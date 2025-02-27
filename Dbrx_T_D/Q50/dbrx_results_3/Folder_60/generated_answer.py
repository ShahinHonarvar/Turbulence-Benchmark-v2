import re

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        sorted_string = ''.join(sorted(re.findall('\\\\w+', string.lower())))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagram_pairs = [(anagrams.count(pair), pair) for pair in set(anagrams)]
    return sum((pair[0] == pair[1] and pair[0] >= 60 for pair in anagram_pairs))