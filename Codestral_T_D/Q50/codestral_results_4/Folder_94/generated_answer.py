from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    anagram_count = 0
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 2:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
            if anagram_count >= 46:
                return True
    return False