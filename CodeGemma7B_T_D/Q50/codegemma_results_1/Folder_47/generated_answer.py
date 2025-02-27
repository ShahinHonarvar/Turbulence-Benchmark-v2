from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_counts = defaultdict(int)
    for s in str_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_counts[sorted_s] += 1
    for count in anagram_counts.values():
        if count >= 47:
            return True
    return False