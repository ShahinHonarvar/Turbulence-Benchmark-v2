from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    anagram_pairs = sum((len(pair) >= 30 for pair in anagrams.values()))
    return anagram_pairs >= 30