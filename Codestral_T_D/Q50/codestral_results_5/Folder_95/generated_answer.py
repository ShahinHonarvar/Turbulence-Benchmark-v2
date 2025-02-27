from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagrams[key].append(s)
    count = sum((len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams))
    return count >= 93