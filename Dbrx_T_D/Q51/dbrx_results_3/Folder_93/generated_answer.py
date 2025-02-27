import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(lambda: collections.Counter())
    for string in strings:
        anagrams[string.lower() if len(string) >= 3 else string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return anagram_pairs <= 36