from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_dict[sorted_word].append(word)
    count = 0
    for anagrams in str_dict.values():
        if len(anagrams) > 1:
            count += len(anagrams) - 1
    return count <= 188