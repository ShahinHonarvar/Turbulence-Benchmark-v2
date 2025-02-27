from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagrams[key].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagrams.values()))
    return anagram_pairs <= 92