from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())

    def has_same_length(word1, word2):
        return len(word1) == len(word2)
    pairs = [(word1, word2) for word1 in lst for word2 in lst if word1 != word2 and has_same_length(word1, word2) and is_anagram(word1, word2) and (len(word1) >= 3)]
    return len(pairs) <= 81