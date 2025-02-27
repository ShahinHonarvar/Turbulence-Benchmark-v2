from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for i, s in enumerate(str_list):
        s = ''.join(sorted([c for c in s.lower() if c.isalpha() and len(c) >= 3]))
        anagrams[s].append(i)
    return len(anagrams) <= 366