from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            key = tuple(sorted(Counter(s).items()))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    anagram_pairs = [len(v) for v in anagrams.values() if len(v) >= 2]
    return sum(anagram_pairs) >= 4