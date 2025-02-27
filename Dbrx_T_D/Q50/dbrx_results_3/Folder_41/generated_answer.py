import itertools

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    anagram_pairs = sum(anagrams.values()) // 2
    return anagram_pairs >= 75