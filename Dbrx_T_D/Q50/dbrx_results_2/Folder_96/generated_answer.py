import collections

def if_contains_anagrams(string_list):
    anagrams = collections.defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    anagram_pairs = 0
    for anagram_list in anagrams.values():
        anagram_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_pairs >= 98