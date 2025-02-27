import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = [string]
        else:
            anagrams[sorted_string].append(string)
    total_anagrams = sum((len(group) for group in anagrams.values() if len(group) >= 2))
    return total_anagrams >= 29