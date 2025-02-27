from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagrams[key].append(word)
    count = 0
    for group in anagrams.values():
        if len(group) >= 2:
            count += len(group) * (len(group) - 1) // 2
    return count >= 78