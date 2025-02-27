import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagrams_count = len(anagrams)
    unique_anagrams = len(set(anagrams))
    return anagrams_count <= 41 * unique_anagrams