from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 2 and len(anagram_list) <= 392:
            return True
    return False