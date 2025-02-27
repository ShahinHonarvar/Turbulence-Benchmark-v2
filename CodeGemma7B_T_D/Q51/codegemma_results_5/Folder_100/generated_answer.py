from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        filtered_word = ''.join((char for char in word if char.isalpha())).lower()
        sorted_word = ''.join(sorted(filtered_word))
        str_dict[sorted_word].append(word)
    return len(str_dict) <= 98