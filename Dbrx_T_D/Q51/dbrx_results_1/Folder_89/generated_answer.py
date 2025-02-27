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
    total_anagrams = sum([1 for value in anagrams.values() if value >= 2])
    return total_anagrams <= 73