from collections import defaultdict

def if_contains_anagrams(str_list):
    word_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_dict[sorted_word].append(word)
    return len(word_dict) <= 50