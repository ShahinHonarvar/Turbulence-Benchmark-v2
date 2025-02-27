from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s] += 1
    count = 0
    for key in anagrams:
        if anagrams[key] > 1:
            count += anagrams[key] * (anagrams[key] - 1) // 2
            if count > 55:
                return False
    return True