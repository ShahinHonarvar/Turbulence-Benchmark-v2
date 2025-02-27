import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    pairs_of_anagrams = sum((anagrams[key] // 2 for key in anagrams if anagrams[key] > 1))
    return pairs_of_anagrams <= 59