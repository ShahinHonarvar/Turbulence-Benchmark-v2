import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        key = ''.join(sorted(string.lower()))
        anagrams[key].append(string)
    pair_count = sum((1 for strings in anagrams.values() if len(strings) >= 2 and len(strings[0]) >= 3))
    return pair_count <= 73