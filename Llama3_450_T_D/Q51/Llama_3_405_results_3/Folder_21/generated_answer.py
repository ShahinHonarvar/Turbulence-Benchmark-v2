from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            anagrams[sorted_str] += 1
    return sum((1 for count in anagrams.values() if count > 1)) <= 26