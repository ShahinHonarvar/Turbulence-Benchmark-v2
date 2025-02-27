import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    anagram_count = 0
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = 1
            else:
                anagram_count += anagrams[sorted_string]
                anagrams[sorted_string] += 1
    return anagram_count >= 106