def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        if len(word1) < 3 or len(word2) < 3:
            return False
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_pairs = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 131:
                    return False
    return True