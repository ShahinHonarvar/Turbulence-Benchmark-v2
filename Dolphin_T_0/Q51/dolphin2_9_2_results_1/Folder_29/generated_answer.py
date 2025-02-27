from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    a_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word in a_dict:
            a_dict[sorted_word] += 1
        else:
            a_dict[sorted_word] = 1
    for val in a_dict.values():
        count += val * (val - 1) // 2
    return count < 319