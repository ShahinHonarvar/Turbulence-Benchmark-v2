import itertools

def if_contains_anagrams(strings_list):
    anagrams = {}
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    pairs_of_anagrams = sum((v // 2 for v in anagrams.values()))
    return pairs_of_anagrams >= 69