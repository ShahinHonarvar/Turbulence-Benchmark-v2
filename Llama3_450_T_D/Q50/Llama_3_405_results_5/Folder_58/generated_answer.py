from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = 0
    for lst in anagrams.values():
        if len(lst) > 1:
            count += len(lst) * (len(lst) - 1) // 2
        if count >= 411:
            return True
    return False