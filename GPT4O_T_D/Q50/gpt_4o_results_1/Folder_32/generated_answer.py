from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = defaultdict(int)
    count = 0
    for string in strings:
        s = string.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams_count[sorted_s] += 1
    for key in anagrams_count:
        count += anagrams_count[key] * (anagrams_count[key] - 1) // 2
    return count >= 194