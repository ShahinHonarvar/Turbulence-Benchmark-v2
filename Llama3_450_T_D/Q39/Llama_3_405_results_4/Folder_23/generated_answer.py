def return_n_greatest_chars(s):
    return sorted(sorted(s)[len(s) - 46:], key=lambda x: x)