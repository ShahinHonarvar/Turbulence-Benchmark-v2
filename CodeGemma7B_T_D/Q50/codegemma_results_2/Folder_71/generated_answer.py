from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 57:
            return True
    return False