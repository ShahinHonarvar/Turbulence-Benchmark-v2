import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    pairs = sum((1 for group in anagrams.values() if len(group) >= 3))
    return pairs <= 75