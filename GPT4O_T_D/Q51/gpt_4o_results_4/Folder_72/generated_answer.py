from itertools import combinations

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = 0
    lower_words = [word.lower() for word in words if len(word) >= 3]
    for word1, word2 in combinations(lower_words, 2):
        if is_anagram(word1, word2):
            anagram_pairs += 1
            if anagram_pairs > 188:
                return False
    return True