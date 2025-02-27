from functools import cmp_to_key

def return_n_greatest_chars(given_str):
    char_dict = {}
    for char in given_str:
        char_dict[char] = ord(char)
    sorted_list = sorted(char_dict.items(), key=cmp_to_key(lambda x, y: y[1] - x[1]))
    return [x[0] for x in sorted_list[:52]]