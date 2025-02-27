from collections import defaultdict

def if_contains_anagrams(str_list):
    seen = defaultdict(list)
    for s in str_list:
        seen[' '.join(sorted(s.lower().replace(' ', '')))].append(s)
    return len(seen) <= 88