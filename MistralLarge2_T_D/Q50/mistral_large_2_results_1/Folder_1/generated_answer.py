from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s].append(s)
    anagram_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values() if len(lst) > 1))
    return anagram_count >= 96