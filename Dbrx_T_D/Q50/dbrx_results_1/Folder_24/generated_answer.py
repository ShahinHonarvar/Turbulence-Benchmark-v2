import itertools

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3

def count_anagrams(words):
    return sum((1 for word in words if is_anagram(word, word)))

def if_contains_anagrams(words):
    words = set(words)
    return count_anagrams(words) >= 65