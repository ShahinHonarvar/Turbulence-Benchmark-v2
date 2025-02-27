import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    anagram_pairs = [pair for pair in anagrams.values() if len(pair) >= 2]
    return len(anagram_pairs) >= 54