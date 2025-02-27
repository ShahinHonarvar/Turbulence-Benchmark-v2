from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    anagram_pairs = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagram_dict.values()))
    return anagram_pairs >= 96