import collections

def if_contains_anagrams(strings_list):
    anagrams = collections.defaultdict(list)
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    count = sum((len(value) > 1 for value in anagrams.values()))
    return count <= 47