from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_counts = defaultdict(int)
    for s in string_list:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_counts[sorted_str] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 233