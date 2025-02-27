import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(lambda: collections.Counter())
    for string in strings:
        string = string.lower()
        if len(string) < 3:
            continue
        anagrams[''.join(sorted(string))].add(string)
    count = sum((1 for group in anagrams.values() if len(group) > 1))
    return count <= 47