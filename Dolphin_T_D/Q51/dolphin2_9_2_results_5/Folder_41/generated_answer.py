from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter_dict = Counter()
    for word in list_of_strings:
        if len(word) > 2:
            sorted_word = ''.join(sorted(word.lower()))
            counter_dict[sorted_word] += 1
    for key, value in counter_dict.items():
        if value > 1:
            counter_dict[key] = 1
    if len(counter_dict) <= 52:
        return True
    else:
        return False