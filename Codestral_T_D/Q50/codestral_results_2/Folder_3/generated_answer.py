from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    count = 0
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 2:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
        if count >= 30:
            return True
    return False