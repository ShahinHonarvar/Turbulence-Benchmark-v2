from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_dict[sorted_word].append(word)
    if len(str_dict) <= 24:
        return True
    return False