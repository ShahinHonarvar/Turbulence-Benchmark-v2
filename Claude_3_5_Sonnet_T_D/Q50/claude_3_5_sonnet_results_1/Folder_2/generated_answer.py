from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
    anagram_count = sum((len(list(combinations(words, 2))) for words in anagram_dict.values() if len(words) > 1))
    return anagram_count >= 246