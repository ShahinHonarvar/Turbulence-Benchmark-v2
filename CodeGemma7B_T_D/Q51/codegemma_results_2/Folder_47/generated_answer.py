from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(int)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    num_anagrams = sum((count >= 2 for count in anagrams.values()))
    return num_anagrams <= 366