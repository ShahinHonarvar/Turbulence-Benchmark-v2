from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return count <= 210