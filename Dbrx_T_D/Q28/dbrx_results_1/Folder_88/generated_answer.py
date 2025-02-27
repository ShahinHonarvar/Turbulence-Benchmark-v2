def return_nth_smallest_ascii(s):
    char_list = [c for c in s if 38 <= s.index(c) <= 64]
    char_list.sort(key=ord)
    return char_list[13]