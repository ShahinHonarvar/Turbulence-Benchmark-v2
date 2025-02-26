def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def is_valid_length(word):
        return len(word) >= 3
    anagram_pairs = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid_length(words[i]) and is_valid_length(words[j]):
                if is_anagram(words[i], words[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 25:
                        return False
    return True