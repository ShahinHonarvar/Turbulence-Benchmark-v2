from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            d[sorted_word].append(word)
    return sum((len(val) > 1 for val in d.values())) >= 21