import collections

def if_contains_anagrams(list_of_strings):
    anagrams = collections.defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    count = 0
    for anagram in anagrams.values():
        if len(anagram) > 1:
            count += len(anagram)
    return count <= 50