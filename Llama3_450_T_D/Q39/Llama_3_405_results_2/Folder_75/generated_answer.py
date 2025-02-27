def return_n_greatest_chars(s):
    ascii_list = sorted([ord(c) for c in s])
    n_greatest_chars = sorted([chr(i) for i in ascii_list[-2:]])
    return n_greatest_chars