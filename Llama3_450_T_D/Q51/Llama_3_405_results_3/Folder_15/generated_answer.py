from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
    count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values() if len(lst) > 1))
    return count <= 20