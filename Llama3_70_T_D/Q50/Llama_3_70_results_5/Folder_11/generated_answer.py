from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(list)
    for s in list_of_strings:
        s_lower = s.lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s_lower))
            anagrams[sorted_str].append(s_lower)
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count >= 28