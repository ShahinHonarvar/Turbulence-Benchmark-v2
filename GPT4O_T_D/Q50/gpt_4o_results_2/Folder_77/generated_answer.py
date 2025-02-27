from collections import defaultdict

def if_contains_anagrams(strings):
    seen = defaultdict(int)
    count = 0
    for s in strings:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s_sorted) >= 3:
            count += seen[s_sorted]
            seen[s_sorted] += 1
        if count >= 209:
            return True
    return False