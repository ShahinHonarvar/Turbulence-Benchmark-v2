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
    total_anagram_pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return total_anagram_pairs >= 21