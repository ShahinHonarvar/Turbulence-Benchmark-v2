import collections

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
        else:
            anagram_dict[sorted_word] = 1
    count = sum((val * (val - 1) // 2 for val in anagram_dict.values()))
    return count >= 84