import re

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        string = re.sub('\\\\W+', '', string).lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    num_anagrams = sum(anagrams.values())
    return num_anagrams >= 2