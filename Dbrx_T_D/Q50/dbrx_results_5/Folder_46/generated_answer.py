import itertools

def if_contains_anagrams(strings_list):
    anagrams_set = set()
    for string_1, string_2 in itertools.combinations(strings_list, 2):
        if len(string_1) >= 3 and len(string_2) >= 3 and (sorted(string_1.lower()) == sorted(string_2.lower())):
            anagrams_set.add(frozenset((string_1.lower(), string_2.lower())))
    return len(anagrams_set) >= 38