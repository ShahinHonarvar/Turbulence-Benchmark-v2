from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = 0
    for v in anagrams.values():
        if len(v) > 1:
            count += 1
        if count > 6:
            return False
    return True