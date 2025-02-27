from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(Counter(sorted_string))
    return len(anagrams) - len(set(anagrams)) <= 8