from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst_strings):
    counter_list = Counter(lst_strings)
    counter_list = {string: Counter(string.lower()) for string in counter_list}
    pairs = combinations(counter_list.items(), 2)
    anagrams = []
    for pair in pairs:
        if sorted(pair[0][1]) == sorted(pair[1][1]):
            anagrams.append(pair)
    return len(anagrams) >= 69