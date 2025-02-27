from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
    anagram_pairs = sum((len(values) * (len(values) - 1) // 2 for values in anagrams.values()))
    return anagram_pairs <= 25