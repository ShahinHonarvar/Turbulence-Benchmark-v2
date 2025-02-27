def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3:
                normalized_word1 = normalize_text(words_list[i])
                normalized_word2 = normalize_text(words_list[j])
                if is_anagram(normalized_word1, normalized_word2):
                    anagram_count += 1
                    if anagram_count > 131:
                        return False
    return True