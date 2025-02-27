import collections

def if_contains_anagrams(strings_list):
    anagrams = collections.defaultdict(list)
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    anagram_pairs = [value for value in anagrams.values() if len(value) > 1]
    return len(anagram_pairs) <= 30