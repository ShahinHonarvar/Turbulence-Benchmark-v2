from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = 0
    for v in anagrams.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
            if count >= 84:
                return True
    return False