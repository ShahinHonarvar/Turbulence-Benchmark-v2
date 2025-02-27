from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(set)
    for s in strings:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(s) >= 3:
            anagram_dict[sorted_str].add(s_lower)
    anagram_count = sum((len(value) * (len(value) - 1) // 2 for value in anagram_dict.values()))
    return anagram_count >= 42