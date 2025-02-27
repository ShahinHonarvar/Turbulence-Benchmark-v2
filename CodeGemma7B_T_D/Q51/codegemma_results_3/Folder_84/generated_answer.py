from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagrams[sorted_str].append(string)
    return len(anagrams) <= 16