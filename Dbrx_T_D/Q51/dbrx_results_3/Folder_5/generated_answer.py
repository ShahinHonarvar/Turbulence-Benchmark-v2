import re

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = re.sub('\\W+', '', string)
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = 1
            else:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] > 4:
                    return False
    return True