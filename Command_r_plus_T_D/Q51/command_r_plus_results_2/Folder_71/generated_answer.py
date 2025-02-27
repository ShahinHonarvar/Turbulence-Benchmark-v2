def if_contains_anagrams(words_list):

    def normalize_text(word):
        return ''.join((char for char in word.lower() if char.isalpha()))

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_pairs = set()
    for idx in range(len(words_list)):
        for other_idx in range(idx + 1, len(words_list)):
            normalized_word1 = normalize_text(words_list[idx])
            normalized_word2 = normalize_text(words_list[other_idx])
            if len(normalized_word1) >= 3 and len(normalized_word2) >= 3:
                if is_anagram(normalized_word1, normalized_word2):
                    anagram_pairs.add(frozenset({words_list[idx], words_list[other_idx]}))
            if len(anagram_pairs) > 9:
                return False
    return True