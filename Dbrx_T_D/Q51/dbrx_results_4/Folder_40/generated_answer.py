from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = set()
    count = 0
    for string in string_list:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            count += 1
            if count > 29:
                return False
        else:
            anagrams.add(sorted_string)
    return True