from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str].append(string)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs >= 5:
            return True
    return False