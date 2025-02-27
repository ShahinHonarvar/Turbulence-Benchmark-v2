from itertools import permutations

def if_contains_anagrams(str_list):
    anagrams = {}
    for word in str_list:
        letters = list(word)
        letters.sort()
        key = ''.join(letters)
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    pairs_of_anagrams = 0
    for values in anagrams.values():
        if len(values) >= 3:
            for perm in permutations(values, r=2):
                pairs_of_anagrams += 1
    return pairs_of_anagrams >= 115