def return_n_greatest_chars(s):
    chars_list = sorted(s, key=lambda x: ord(x), reverse=True)[:26]
    chars_list.sort(reverse=True)
    return chars_list