from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for string_ in map(str.lower, string_list):
        sorted_string = ''.join(sorted(string_))
        anagrams[sorted_string].append(string_)
    return sum((len(value) > 3 and len(value) == 66 for value in anagrams.values())) <= 1