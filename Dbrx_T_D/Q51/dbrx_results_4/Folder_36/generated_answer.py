import collections

def if_contains_anagrams(string_list):
    anagrams = collections.defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    anagram_pairs = sum((len(value) >= 3 for value in anagrams.values()))
    return anagram_pairs <= 25