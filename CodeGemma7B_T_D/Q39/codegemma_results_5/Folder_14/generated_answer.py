def return_n_greatest_chars(ch):
    ascii_values = sorted(zip(map(ord, ch), ch), reverse=True)
    return [char for _, char in ascii_values[:69]]