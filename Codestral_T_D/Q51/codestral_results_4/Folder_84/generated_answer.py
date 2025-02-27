from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            d[sorted_word].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in d.values()))
    return anagram_pairs <= 16