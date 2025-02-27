from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams_dict = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams_dict[sorted_string].append(string)
    count = 0
    for sorted_string, anagrams in anagrams_dict.items():
        n = len(anagrams)
        count += n * (n - 1) // 2
    if count <= 475:
        return True
    else:
        return False