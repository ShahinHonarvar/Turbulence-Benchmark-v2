from itertools import combinations

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_pairs = [(word1, word2) for word1, word2 in combinations(words, 2) if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2)]
    return len(anagram_pairs) <= 445