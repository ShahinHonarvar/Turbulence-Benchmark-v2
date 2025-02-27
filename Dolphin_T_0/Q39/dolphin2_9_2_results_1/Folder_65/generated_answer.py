def return_n_greatest_chars(s):
    chars_list = list(s)
    chars_list_sorted = sorted(chars_list, key=lambda x: ord(x), reverse=True)
    result = chars_list_sorted[:27]
    return result