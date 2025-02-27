import string

def sorted_str(s):
    return ''.join(sorted(s.lower()))

def is_anagram(s1, s2):
    return sorted_str(s1) == sorted_str(s2)

def count_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = sorted_str(word)
        if sorted_word in anagrams:
            anagrams[sorted_word] += 1
        else:
            anagrams[sorted_word] = 1
    return sum(anagrams.values()) // 2

def if_contains_anagrams(words):
    return count_anagrams(words) >= 5