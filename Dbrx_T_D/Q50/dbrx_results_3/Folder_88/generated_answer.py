import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = set()
            anagrams[sorted_string].add(string)
    for group in anagrams.values():
        if len(group) >= 2:
            pairs = sum((1 for _ in itertools.combinations(group, 2)))
            if pairs >= 34:
                return True
    return False