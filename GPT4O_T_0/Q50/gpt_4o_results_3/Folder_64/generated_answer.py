from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str].append(string)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs >= 5