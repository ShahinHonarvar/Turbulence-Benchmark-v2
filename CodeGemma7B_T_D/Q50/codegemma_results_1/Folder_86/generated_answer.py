from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_count = defaultdict(set)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word].add(word)
    for group in anagram_count.values():
        if len(group) >= 115:
            return True
    return False