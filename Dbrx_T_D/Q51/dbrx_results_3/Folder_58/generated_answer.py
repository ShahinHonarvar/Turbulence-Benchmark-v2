import re

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(re.findall('\\b\\w+\\b', string.lower())))
            if sorted_string in anagrams:
                pairs = len(anagrams) - len(list(filter(lambda x: len(x) < 3, anagrams))) // 2
                if pairs > 60:
                    return False
                else:
                    continue
            anagrams.add(sorted_string)
    return True