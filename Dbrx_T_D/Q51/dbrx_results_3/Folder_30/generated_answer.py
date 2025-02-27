import collections

def if_contains_anagrams(string_list):
    anagrams = collections.defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    anagram_pairs = [value for value in anagrams.values() if len(value) >= 3]
    return len(anagram_pairs) <= 28