from collections import Counter

def if_contains_anagrams(strings_list):
    anagrams = {}
    for string in strings_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    return True if sum(anagrams.values()) >= 26 else False