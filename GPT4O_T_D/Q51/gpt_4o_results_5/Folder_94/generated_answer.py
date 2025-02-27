from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        normalized = ''.join(sorted(string.lower()))
        if len(normalized) >= 3:
            anagram_dict[normalized].append(string)
    anagram_count = 0
    for anagram_list in anagram_dict.values():
        n = len(anagram_list)
        if n > 1:
            anagram_count += n * (n - 1) // 2
        if anagram_count > 181:
            return False
    return True