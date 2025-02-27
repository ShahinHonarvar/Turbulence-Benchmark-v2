import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    pairs = sum((1 for group in anagrams.values() if len(group) >= 2))
    return pairs <= 6