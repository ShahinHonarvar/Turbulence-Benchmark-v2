from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    anagram_pairs = 0
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs >= 39:
            return True
    return False