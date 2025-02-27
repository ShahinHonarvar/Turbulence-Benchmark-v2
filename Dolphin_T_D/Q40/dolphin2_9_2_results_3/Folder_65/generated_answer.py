def return_n_smallest_chars(s):
    chars_list = [c for c in s]
    chars_list = sorted(chars_list, key=lambda x: ord(x), reverse=True)
    return chars_list[:27]