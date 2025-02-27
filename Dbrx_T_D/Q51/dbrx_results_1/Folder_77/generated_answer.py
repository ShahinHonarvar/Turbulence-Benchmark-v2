import collections

def if_contains_anagrams(list_of_strings):
    anagrams = collections.defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    anagram_pairs = [pair for pair in anagrams.values() if len(pair) >= 3]
    return len(anagram_pairs) <= 17