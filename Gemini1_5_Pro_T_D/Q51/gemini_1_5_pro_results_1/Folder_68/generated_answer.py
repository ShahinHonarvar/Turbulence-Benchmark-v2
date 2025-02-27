from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(list)
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    count = 0
    for key in anagrams:
        length = len(anagrams[key])
        if length >= 2:
            count += length * (length - 1) // 2
    return count <= 94