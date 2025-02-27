from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_count = defaultdict(int)
    for s in str_list:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_count[sorted_str] += 1
    count = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return count <= 55