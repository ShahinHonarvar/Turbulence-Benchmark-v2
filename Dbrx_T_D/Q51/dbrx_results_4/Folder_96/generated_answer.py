import re

def if_contains_anagrams(strings):
    anagrams = {}
    pairs = 0
    for string in strings:
        string = re.sub('[^\\w]', '', string).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] == 2:
                pairs += 1
                if pairs > 2:
                    return False
        else:
            anagrams[sorted_string] = 1
    return pairs <= 2