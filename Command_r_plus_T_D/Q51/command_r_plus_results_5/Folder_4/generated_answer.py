def if_contains_anagrams(words_list):

    def normalize_text(text):
        return ''.join((e for e in text if e.isalpha())).lower()

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    words_set = set(words_list)
    for word1 in words_set:
        for word2 in words_set:
            if word1 != word2 and is_anagram(normalize_text(word1), normalize_text(word2)) and (len(word1) >= 3):
                anagram_count += 1
                if anagram_count > 84:
                    return False
    return True