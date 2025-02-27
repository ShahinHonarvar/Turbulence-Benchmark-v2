import itertools
import string

def if_contains_anagrams(string_list):
    anagrams = [word.lower() for word in string_list if len(set(word.lower())) == len(word.lower())]
    anagram_pairs = [(word, ''.join(sorted(word))) for word in anagrams if len(word) >= 3]
    return len(list(itertools.combinations(anagram_pairs, 2))) <= 86