from itertools import permutations

def if_contains_anagrams(str_list):
    anagrams = set()
    for string in str_list:
        string = sorted(string.lower())
        if len(string) < 3:
            continue
        for permutation in permutations(string):
            anagrams.add(''.join(permutation))
    return len(anagrams) <= 40