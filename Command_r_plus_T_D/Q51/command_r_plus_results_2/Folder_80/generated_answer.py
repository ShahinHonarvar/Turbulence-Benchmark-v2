def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower().strip()

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word_i = normalize_text(words_list[i])
            word_j = normalize_text(words_list[j])
            if len(word_i) >= 3 and len(word_j) >= 3 and is_anagram(word_i, word_j):
                anagram_pair = tuple(sorted((word_i, word_j)))
                if anagram_pair not in anagram_pairs:
                    anagram_pairs.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count > 255:
                        return False
    return True