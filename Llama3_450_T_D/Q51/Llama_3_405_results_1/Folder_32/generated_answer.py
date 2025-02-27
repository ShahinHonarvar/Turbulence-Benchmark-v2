from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            anagrams[sorted_str].append(s)
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
        if count > 89:
            return False
    return True