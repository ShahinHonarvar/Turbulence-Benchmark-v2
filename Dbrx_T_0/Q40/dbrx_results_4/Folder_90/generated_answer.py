def return_n_smallest_chars(string):
    chars_list = sorted(list(string), key=ord)[:24]
    chars_list.sort(reverse=True)
    return chars_list