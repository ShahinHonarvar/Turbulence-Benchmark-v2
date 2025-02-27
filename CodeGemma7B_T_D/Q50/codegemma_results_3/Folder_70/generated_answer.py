from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    count = 0
    for anag in anagrams.values():
        count += len(anag) * (len(anag) - 1) // 2
    return count >= 189