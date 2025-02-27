import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = 1
            else:
                anagrams[sorted_string] += 1
    total_anagrams = sum(anagrams.values())
    return total_anagrams >= 143