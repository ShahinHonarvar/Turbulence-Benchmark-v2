import collections

def if_contains_anagrams(strings_list):
    anagrams_counter = 0
    anagrams_dictionary = collections.defaultdict(list)
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams_dictionary[sorted_string].append(string)
    for anagram in anagrams_dictionary.values():
        if len(anagram) >= 3:
            anagrams_counter += len(anagram) - 1
    return anagrams_counter >= 41