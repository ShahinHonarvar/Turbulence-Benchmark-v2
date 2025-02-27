import re

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        string = re.sub('\\W+', '', string).lower()
        sorted_string = ''.join(sorted(string))
        if len(string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] > 1 and sum(anagrams.values()) > 407:
                    return True
            else:
                anagrams[sorted_string] = 1
    return False