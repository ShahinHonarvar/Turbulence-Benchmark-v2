def return_nth_smallest_ascii(s):
    char_list = sorted([c for i, c in enumerate(s) if 46 <= i <= 82])
    return char_list[15]