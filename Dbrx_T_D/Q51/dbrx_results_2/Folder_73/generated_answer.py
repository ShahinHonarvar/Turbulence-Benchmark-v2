import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    pairs = sum((len(values) // 2 for values in anagrams.values()))
    return pairs <= 279