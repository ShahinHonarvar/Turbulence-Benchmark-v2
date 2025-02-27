import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    pair_count = sum([val // 2 for val in anagrams.values()])
    return pair_count >= 77