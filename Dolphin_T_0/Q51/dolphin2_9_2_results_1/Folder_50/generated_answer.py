from collections import Counter
    from itertools import combinations

def if_contains_anagrams(list_of_strings):
    list_of_strings = [string.lower() for string in list_of_strings]
    list_of_strings = [string for string in list_of_strings if len(string) >= 3]
    list_of_strings = [''.join(sorted(string)) for string in list_of_strings]
    counter = Counter(list_of_strings)
    list_of_pairs = list(combinations(counter.elements(), 2))
    if len(list_of_pairs) <= 47:
        return True
    else:
        return False