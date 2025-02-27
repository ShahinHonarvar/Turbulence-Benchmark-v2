import re

def if_contains_anagrams(strings_list):
    anagrams = {}
    anagram_pairs = 0
    for string in strings_list:
        sorted_string = ''.join(sorted(re.findall('[a-z]', string.lower())))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] == 2:
                    anagram_pairs += 1
            else:
                anagrams[sorted_string] = 1
    return anagram_pairs <= 416