from collections import defaultdict

def if_contains_anagrams(str_list):
    str_count = defaultdict(int)
    for s in str_list:
        sorted_s = ''.join(sorted(s.lower()))
        str_count[sorted_s] += 1
    anagram_pairs = 0
    for count in str_count.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 69