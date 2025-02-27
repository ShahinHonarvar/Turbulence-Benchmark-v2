def return_n_smallest_chars(s):
    char_list = [c for c in s]
    char_list.sort(key=lambda c: ord(c))
    return char_list[:77]