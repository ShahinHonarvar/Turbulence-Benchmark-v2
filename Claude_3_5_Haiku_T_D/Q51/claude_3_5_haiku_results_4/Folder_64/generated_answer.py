def if_contains_anagrams(words):

    def is_valid_anagram(word1, word2):
        return len(word1) >= 3 and len(word1) == len(word2) and (sorted(word1.lower()) == sorted(word2.lower()))
    anagram_pairs = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 59:
                    return False
    return True