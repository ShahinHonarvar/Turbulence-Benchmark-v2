import itertools

def if_contains_anagrams(strings_list):
    anagrams_dict = {}
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams_dict:
                anagrams_dict[sorted_string] = []
            anagrams_dict[sorted_string].append(string)
    anagram_pairs = 0
    for anagram_list in anagrams_dict.values():
        if len(anagram_list) >= 2:
            anagram_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_pairs >= 188