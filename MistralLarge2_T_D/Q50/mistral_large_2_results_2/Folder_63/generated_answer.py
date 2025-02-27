from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_count[sorted_string] += 1
    count_anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if v > 1))
    return count_anagram_pairs >= 89