def if_contains_anagrams(words_list):

    def normalize_text(text):
        return ''.join((e for e in text if e.isalpha())).lower()

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word1 = normalize_text(words_list[i])
            word2 = normalize_text(words_list[j])
            if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
                anagram_pair = tuple(sorted([words_list[i], words_list[j]]))
                if anagram_pair not in anagram_pairs:
                    anagram_pairs.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count > 64:
                        return False
    return True