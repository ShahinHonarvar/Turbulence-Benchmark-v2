from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(int)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word] += 1
    for count in anagram_dict.values():
        if count > 173:
            return False
    return True