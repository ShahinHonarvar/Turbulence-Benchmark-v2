from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams_dict = defaultdict(lambda: [])
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams_dict[sorted_string].append(string)
    count = 0
    for key in anagrams_dict:
        n = len(anagrams_dict[key])
        count += n * (n - 1) // 2
    return count <= 257