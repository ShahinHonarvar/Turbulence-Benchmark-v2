from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for string in lst:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str].append(string)
    count = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values() if len(value) > 1))
    return count >= 30