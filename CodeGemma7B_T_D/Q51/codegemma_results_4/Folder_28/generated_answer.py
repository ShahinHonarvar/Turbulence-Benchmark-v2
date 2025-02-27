def if_contains_anagrams(list_of_strings):
    anagrams_sets = set()
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams_sets.add(sorted_string)
    return len(anagrams_sets) <= 78