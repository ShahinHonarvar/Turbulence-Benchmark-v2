from itertools import combinations

def if_contains_anagrams(str_list):
    list_of_anagrams = [sorted(s.lower()) for s in str_list if len(s) >= 3]
    combinations_of_26_pairs = combinations(list_of_anagrams, 26)
    return any((all((a == b for a, b in pair)) for pair in combinations_of_26_pairs))