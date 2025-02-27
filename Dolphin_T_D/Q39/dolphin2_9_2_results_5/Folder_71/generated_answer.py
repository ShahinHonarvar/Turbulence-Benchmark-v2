def return_n_greatest_chars(s):
    list_s = sorted(list(s), key=lambda x: ord(x))
    return sorted(list_s[-14:])