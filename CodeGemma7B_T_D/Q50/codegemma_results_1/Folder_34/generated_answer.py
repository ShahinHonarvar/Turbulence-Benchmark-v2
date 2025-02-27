from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        clean_word = ''.join(sorted(word.lower()))
        str_dict[clean_word].append(word)
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 25:
            return True
    return False