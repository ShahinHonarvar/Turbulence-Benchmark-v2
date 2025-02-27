from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return count >= 43