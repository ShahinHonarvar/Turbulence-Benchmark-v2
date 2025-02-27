from collections import defaultdict, Counter

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        if len(string) >= 3 and all((c.isalpha() for c in string)):
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    return len(anagrams) <= 47