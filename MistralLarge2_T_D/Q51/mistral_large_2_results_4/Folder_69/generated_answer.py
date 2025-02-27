from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagrams[key].append(string)
    anagram_pairs = sum((1 for group in anagrams.values() if len(group) > 1))
    return anagram_pairs <= 58