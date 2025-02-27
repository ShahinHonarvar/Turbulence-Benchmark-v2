import itertools

def if_contains_anagrams(strings):

    def is_anagram(word1, word2):
        return len(word1) == len(word2) and sorted(word1.lower()) == sorted(word2.lower())
    return sum((is_anagram(word1, word2) for word1, word2 in itertools.combinations(strings, 2) if len(word1) >= 3 and len(word2) >= 3)) >= 79