import itertools

def if_contains_anagrams(strings_list):
    anagrams = {}
    for string in strings_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    total_anagrams = sum([count // 2 for count in anagrams.values()])
    return total_anagrams >= 61