import collections

def if_contains_anagrams(str_list):
    anagrams = collections.defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagrams[sorted_str].append(string)
    return len(anagrams) <= 85