from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_str_count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        sorted_str_count[sorted_str] += 1
    anagram_pairs_count = sum((count * (count - 1) // 2 for count in sorted_str_count.values()))
    return anagram_pairs_count >= 21