def if_contains_anagrams(list_strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in list_strings if len(s) >= 3]
    count = len(sorted_strings)
    distinct_pairs = len(set(sorted_strings))
    pairs = count - distinct_pairs
    return pairs <= 48