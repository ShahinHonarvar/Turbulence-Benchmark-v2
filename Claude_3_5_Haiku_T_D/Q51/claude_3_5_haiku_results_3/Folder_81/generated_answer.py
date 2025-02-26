def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        cleaned_word1 = ''.join(sorted((char.lower() for char in word1 if char.isalpha())))
        cleaned_word2 = ''.join(sorted((char.lower() for char in word2 if char.isalpha())))
        return cleaned_word1 == cleaned_word2 and len(cleaned_word1) >= 3
    anagram_pairs = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if is_anagram(word_list[i], word_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 79:
                    return False
    return True