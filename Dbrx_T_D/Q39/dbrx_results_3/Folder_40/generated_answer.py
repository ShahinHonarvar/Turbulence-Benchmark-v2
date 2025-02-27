def return_n_greatest_chars(string_of_chars):
    chars_list = list(string_of_chars)
    chars_list = list(dict.fromkeys(chars_list))
    chars_list.sort(reverse=True)
    if len(chars_list) < 7:
        return chars_list
    return chars_list[:7]