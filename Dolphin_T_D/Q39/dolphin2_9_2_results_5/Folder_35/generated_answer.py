def return_n_greatest_chars(s):
    return sorted([_ for _ in s if _ in string.ascii_letters()][-7:])