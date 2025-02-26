def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def is_valid_anagram(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and (word1.lower() != word2.lower()) and is_anagram(word1, word2)
    anagram_pairs = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if is_valid_anagram(word_list[i], word_list[j]):
                anagram_pairs += 1
    return anagram_pairs <= 40