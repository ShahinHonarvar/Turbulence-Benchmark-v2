from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            d[sorted_word].append(word)
    anagram_pairs = sum((len(value) * (len(value) - 1) // 2 for value in d.values()))
    return anagram_pairs >= 42