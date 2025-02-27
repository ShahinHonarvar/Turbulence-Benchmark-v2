import collections

def if_contains_anagrams(strings):
    anagrams_count = 0
    anagrams = collections.defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    for anagram in anagrams.values():
        if len(anagram) >= 177:
            anagrams_count += 1
    return anagrams_count >= 1