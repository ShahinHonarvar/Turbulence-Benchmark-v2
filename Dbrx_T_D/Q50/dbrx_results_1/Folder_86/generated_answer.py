import string

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = tuple(sorted(s.lower()))
        if len(sorted_s) >= 3:
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s].append(s)
    anagram_pairs = sum((len(ana) * (len(ana) - 1) // 2 for ana in anagrams.values()))
    return anagram_pairs >= 115