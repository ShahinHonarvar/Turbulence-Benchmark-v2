def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def is_valid_length(word):
        return len(word) >= 3
    anagram_pairs = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if is_valid_length(word_list[i]) and is_valid_length(word_list[j]) and is_anagram(word_list[i], word_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 47:
                    return False
    return True