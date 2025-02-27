from collections import defaultdict
from itertools import combinations_with_replacement as cwr

def if_contains_anagrams(str_list):
    letters_to_anagrams = defaultdict(list)
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = sorted(word.lower())
        letters_to_anagrams[''.join(sorted_word)].append(word.lower())
    count = 0
    for anagram_list in letters_to_anagrams.values():
        if len(anagram_list) >= 96:
            count += len(anagram_list)
    return count >= 96