from collections import Counter

def if_contains_anagrams(strings):
    anagrams = 0
    for string in strings:
        if len(string) >= 3 and Counter(string.lower()) in [Counter(word.lower()) for word in strings]:
            anagrams += 1
    return anagrams // 2 <= 14