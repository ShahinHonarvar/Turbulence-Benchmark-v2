import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = 1
            else:
                anagrams[sorted_string] += 1
    anagram_pairs = sum([count // 2 for count in anagrams.values()])
    return anagram_pairs >= 24