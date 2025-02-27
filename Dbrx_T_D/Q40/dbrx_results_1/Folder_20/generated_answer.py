def return_n_smallest_chars(string_of_chars):
    ascii_list = list(map(ord, string_of_chars))
    sorted_list = sorted(ascii_list)[:40]
    return list(map(chr, sorted_list))