import collections

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagrams = collections.defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    for anagram in anagrams.values():
        if len(anagram) >= 3:
            anagram_count += len(anagram) * (len(anagram) - 1) // 2
    return anagram_count >= 277