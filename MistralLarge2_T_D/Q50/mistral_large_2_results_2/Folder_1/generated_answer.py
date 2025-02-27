from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagrams[key].append(s)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagrams.values()))
    return anagram_pairs >= 96