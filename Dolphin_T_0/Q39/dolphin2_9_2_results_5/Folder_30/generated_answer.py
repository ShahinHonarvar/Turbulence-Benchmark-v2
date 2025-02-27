def return_n_greatest_chars(s):
    chars_list = list(s)
    chars_list.sort(reverse=True)
    chars_list = chars_list[:72]
    chars_list.sort()
    return chars_list