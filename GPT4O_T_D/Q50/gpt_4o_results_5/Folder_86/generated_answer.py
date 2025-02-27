from collections import defaultdict

def if_contains_anagrams(strings):
    str_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            str_dict[sorted_str] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in str_dict.values()))
    return anagram_pairs >= 115