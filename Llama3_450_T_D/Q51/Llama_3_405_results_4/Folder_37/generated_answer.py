from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            anagrams[sorted_str].append(s)
    count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values()))
    return count <= 206