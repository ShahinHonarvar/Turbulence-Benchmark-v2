import itertools

def if_contains_anagrams(strings_list):
    anagrams = {}
    for string in strings_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    anagram_pairs = 0
    for anagram in anagrams.values():
        if anagram >= 2:
            anagram_pairs += anagram * (anagram - 1) // 2
    return anagram_pairs >= 411