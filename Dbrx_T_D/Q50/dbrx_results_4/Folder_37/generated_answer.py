import collections

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    count = sum(anagrams.values()) - len(anagrams)
    return count >= 29