import sys

def sort_string(s):
    return ''.join(sorted(s.lower()))

def is_anagram(s1, s2):
    return sort_string(s1) == sort_string(s2)

def count_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        sorted_word = sort_string(word)
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                anagrams[sorted_word] += 1
                count += 1
    return count

def if_contains_anagrams(words):
    return count_anagrams(words) >= 4