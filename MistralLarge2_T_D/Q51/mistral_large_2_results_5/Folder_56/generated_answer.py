from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    anagram_count = sum((1 for group in anagrams.values() if len(group) > 1))
    return anagram_count <= 11