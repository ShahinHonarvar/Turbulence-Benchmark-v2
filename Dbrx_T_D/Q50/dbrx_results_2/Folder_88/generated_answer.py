import itertools

def if_contains_anagrams(strings_list):
    anagrams = {}
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
    anagram_pairs = sum((len(value) // 2 for value in anagrams.values()))
    return anagram_pairs >= 34