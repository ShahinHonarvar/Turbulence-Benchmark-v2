def return_n_greatest_chars(s):
    return sorted([char for char in set(s)], key=lambda x: ord(x), reverse=True)[:49]