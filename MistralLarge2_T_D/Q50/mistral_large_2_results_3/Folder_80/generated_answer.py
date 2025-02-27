from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    anagram_count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams[0]) >= 3 and len(anagrams) > 1:
            anagram_count += len(anagrams) - 1
    return anagram_count >= 19