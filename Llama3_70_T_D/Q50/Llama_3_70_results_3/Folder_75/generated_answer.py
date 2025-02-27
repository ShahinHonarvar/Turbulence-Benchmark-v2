from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagram_dict[sorted_string] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 70