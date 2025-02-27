from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())
    pairs = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                pairs += 1
                if pairs > 44:
                    return False
    return True