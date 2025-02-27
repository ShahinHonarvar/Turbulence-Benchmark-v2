from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str] += 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return total_pairs >= 92