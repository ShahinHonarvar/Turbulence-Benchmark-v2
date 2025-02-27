def if_contains_anagrams(words_list):

    def normalize_text(word):
        return ''.join(filter(str.isalpha, word)).lower()

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    words_set = set(map(normalize_text, words_list))
    for word1 in words_set:
        for word2 in words_set:
            if is_anagram(word1, word2) and len(word1) >= 3 and (word1 != word2):
                anagram_count += 1
                if anagram_count > 474:
                    return False
    return True