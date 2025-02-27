def return_n_smallest_chars(string_arg):
    chars_list = sorted(list(set(string_arg)), key=ord)[:3]
    chars_list.sort(key=ord, reverse=True)
    return chars_list