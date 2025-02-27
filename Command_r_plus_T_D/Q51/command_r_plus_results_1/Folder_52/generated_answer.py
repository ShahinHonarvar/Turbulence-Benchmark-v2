def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    words_set = {normalize_text(word) for word in words_list}
    for word1 in words_set:
        for word2 in words_set:
            if is_anagram(word1, word2) and len(word1) >= 3 and (word1 != word2):
                anagram_count += 1
                if anagram_count > 43:
                    return False
                break
    return True