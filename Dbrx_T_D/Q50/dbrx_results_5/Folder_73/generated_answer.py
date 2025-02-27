import itertools

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    total_anagrams = sum(anagrams.values()) // 2
    return total_anagrams >= 91