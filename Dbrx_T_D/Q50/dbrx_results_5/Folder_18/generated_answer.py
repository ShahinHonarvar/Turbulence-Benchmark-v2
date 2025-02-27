import numpy as np

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagram_counts = np_Array(anagrams).value_counts()
    return anagram_counts[anagram_counts >= 2].sum() >= 106