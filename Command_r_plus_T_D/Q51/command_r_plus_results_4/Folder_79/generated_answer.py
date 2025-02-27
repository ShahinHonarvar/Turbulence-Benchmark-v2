def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word1, word2 = (normalize_text(words_list[i]), normalize_text(words_list[j]))
            if is_anagram(word1, word2) and len(word1) >= 3:
                anagram_count += 1
                if anagram_count > 173:
                    return False
    return True