from collections import Counter

def if_contains_anagrams(list_of_strings):
    pre_sorted_words = [''.join(sorted(i.lower())) for i in list_of_strings if len(i) >= 3]
    count_dict = dict(Counter(pre_sorted_words))
    count_list = list(count_dict.values())
    result = False
    for i in count_list:
        if i >= 2:
            result = True
    return result