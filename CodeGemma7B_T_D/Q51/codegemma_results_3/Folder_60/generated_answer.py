from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_dict[sorted_word].append(word)
    anagram_count = 0
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 3:
            anagram_count += combination_count(len(anagram_list))
    return anagram_count <= 77

def combination_count(n):
    return n * (n - 1) // 2

def test_if_contains_anagrams():
    assert if_contains_anagrams([]) == True
    assert if_contains_anagrams(['a', 'b', 'c']) == True
    assert if_contains_anagrams(['a', 'ab', 'ac', 'abc']) == True
    assert if_contains_anagrams(['a', 'ab', 'ac', 'abc', 'bcd', 'bdc', 'cdc', 'dcb']) == False