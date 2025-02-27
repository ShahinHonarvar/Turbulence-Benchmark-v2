def if_contains_anagrams(list_of_strings):
    anagrams_count = {}
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted([c for c in string.lower() if c.isalpha()]))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    pairs_count = sum((value * (value - 1) // 2 for value in anagrams_count.values()))
    return pairs_count <= 54