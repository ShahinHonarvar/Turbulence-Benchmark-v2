import collections

def if_contains_anagrams(string_list):
    anagrams = collections.defaultdict(lambda: collections.Counter())
    for string in string_list:
        sorted_string = ''.join(sorted(filter(str.isalpha, string.lower())))
        if len(sorted_string) < 3:
            continue
        anagrams[sorted_string] += 1
    return sum((v * (v - 1) // 2 for v in anagrams.values())) <= 75