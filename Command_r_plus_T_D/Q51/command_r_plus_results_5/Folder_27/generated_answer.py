def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word1, word2 = (normalize_text(words_list[i]), normalize_text(words_list[j]))
            if is_anagram(word1, word2) and len(word1) >= 3:
                anagram_pairs.add(frozenset([word1, word2]))
            if len(anagram_pairs) > 113:
                return False
    return True