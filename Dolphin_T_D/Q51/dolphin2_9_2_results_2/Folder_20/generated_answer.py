from collections import Counter

def if_contains_anagrams(lst_of_strings):
    counter_dict = {}
    for word in lst_of_strings:
        if len(word) < 3:
            continue
        counter_dict[word.lower()] = Counter(word.lower())
    lst = list(counter_dict.values())
    counter_values = set()
    for counter in lst:
        d = dict(counter)
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
        counter_values.add(frozenset(d.items()))
    if_contains = len(counter_values) > 10 ** 6
    return if_contains