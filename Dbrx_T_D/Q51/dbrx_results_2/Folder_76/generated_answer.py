import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    anagram_pairs = sum((len(group) // 2 for group in anagrams.values() if len(group) >= 3))
    return anagram_pairs <= 91