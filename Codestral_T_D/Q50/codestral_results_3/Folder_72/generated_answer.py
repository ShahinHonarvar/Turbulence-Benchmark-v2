from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    anagram_count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 2:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 55