def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        word1 = ''.join(sorted(word1.lower()))
        word2 = ''.join(sorted(word2.lower()))
        return word1 == word2

    def is_valid_length(word):
        return len(word) >= 3
    valid_words = [word for word in word_list if is_valid_length(word)]
    anagram_pairs = 0
    for i in range(len(valid_words)):
        for j in range(i + 1, len(valid_words)):
            if is_anagram(valid_words[i], valid_words[j]):
                anagram_pairs += 1
                if anagram_pairs > 40:
                    return False
    return True