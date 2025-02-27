def return_nth_smallest_ascii(s):
    ascii_list = sorted(list(set(s)))[:9]
    return ascii_list[8]