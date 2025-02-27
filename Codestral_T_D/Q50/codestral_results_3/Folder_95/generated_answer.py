from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            d[sorted_word].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in d.values()))
    return anagram_pairs >= 93