from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[''.join(sorted(s.lower()))].append(s)
    anagram_pairs = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_dict.values()))
    return anagram_pairs <= 93