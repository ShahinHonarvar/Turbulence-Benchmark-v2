def return_n_greatest_chars(arg1):
    return sorted(arg1, key=lambda x: ord(x), reverse=True)[:77]