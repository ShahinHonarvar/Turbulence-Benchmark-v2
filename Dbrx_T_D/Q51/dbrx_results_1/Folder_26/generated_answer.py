from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = []
    string_list = [string.lower() for string in string_list if len(string) >= 3]
    for string in string_list:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagrams:
            anagrams.append(sorted_string)
    return len(Counter(anagrams).keys()) <= 35