from collections import Counter

def if_contains_anagrams(lst):
    a_dict = {}
    for word in lst:
        if len(word) >= 3:
            clean_word = word.lower()
            sorted_word = ''.join(sorted(clean_word))
            if sorted_word not in a_dict:
                a_dict[sorted_word] = 1
            else:
                a_dict[sorted_word] += 1
    return any((value >= 2 for value in a_dict.values()))