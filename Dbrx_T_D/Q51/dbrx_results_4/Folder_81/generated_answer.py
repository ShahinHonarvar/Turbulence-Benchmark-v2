import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            anagrams[''.join(sorted(string))].append(string)
    return sum((len(anagrams[i]) > 1 for i in anagrams)) <= 79