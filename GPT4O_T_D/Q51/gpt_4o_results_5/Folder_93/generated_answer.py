from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_count[sorted_str] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pair_count <= 36