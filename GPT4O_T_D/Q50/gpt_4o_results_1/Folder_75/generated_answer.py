from collections import Counter

def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_tuple = tuple(sorted(string.lower()))
        if sorted_tuple in anagram_dict:
            anagram_dict[sorted_tuple] += 1
        else:
            anagram_dict[sorted_tuple] = 1
    count = sum((v * (v - 1) // 2 for v in anagram_dict.values() if v > 1))
    return count >= 70