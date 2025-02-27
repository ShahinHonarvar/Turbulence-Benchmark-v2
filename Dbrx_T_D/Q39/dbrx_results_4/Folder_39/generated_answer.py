def return_n_greatest_chars(s):
    return sorted(list(s), key=chr)[len(s) - 23:]