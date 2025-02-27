from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            str_dict[sorted_word].append(word)
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 123:
            return True
    return False