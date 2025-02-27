import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = set()
            anagrams[sorted_string].add(string)
    anagram_pairs = 0
    for value in anagrams.values():
        anagram_pairs += sum((1 for _ in itertools.combinations(value, 2)))
        if anagram_pairs >= 153:
            return True
    return False