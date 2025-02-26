def if_contains_anagrams(words):

    def is_valid_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def is_valid_string(word):
        return len(word) >= 3 and word.isalpha()
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_valid_string(words[i]) and is_valid_string(words[j]) and is_valid_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 40:
                    return False
    return True