from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        if len(word) < 3 or not word.isascii():
            continue
        sorted_word = ''.join(sorted(word.lower()))
        str_dict[sorted_word].append(word)
    num_pairs = 0
    for word_list in str_dict.values():
        num_pairs += len(word_list) * (len(word_list) - 1) // 2
    return num_pairs <= 113