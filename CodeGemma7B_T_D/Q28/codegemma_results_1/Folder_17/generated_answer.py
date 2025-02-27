def return_nth_smallest_ascii(char_str):
    chars_range_4_33 = [ch for ch in char_str[4:34]]
    return sorted(chars_range_4_33, key=ord)[3]