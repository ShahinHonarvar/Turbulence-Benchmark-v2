import re

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def count_anagrams(words):
    return sum((1 for word in words if len(word) >= 3 and is_anagram(word, word[::-1])))

def if_contains_anagrams(words):
    anagram_count = count_anagrams(words)
    return anagram_count <= 2