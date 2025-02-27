from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for string in strings:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) >= 3:
            key = ''.join(sorted(string))
            anagrams[key] += 1
    return sum((value - 1 for value in anagrams.values())) <= 14