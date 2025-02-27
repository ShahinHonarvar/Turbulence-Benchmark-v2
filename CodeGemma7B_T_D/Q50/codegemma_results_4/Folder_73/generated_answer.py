from collections import defaultdict

def if_contains_anagrams(str_list):
    str_tuples = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            str_tuples[sorted_string].append(string)
    pairs_count = 0
    for anagrams in str_tuples.values():
        pairs_count += len(anagrams) * (len(anagrams) - 1) // 2
    return pairs_count >= 91