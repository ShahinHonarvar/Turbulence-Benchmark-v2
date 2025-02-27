def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    words_set = set(words_list)
    for word1 in words_set:
        for word2 in words_set:
            if word1 != word2 and is_anagram(normalize_text(word1), normalize_text(word2)) and (len(word1) >= 3):
                anagram_count += 1
                if anagram_count > 68:
                    return False
    return True