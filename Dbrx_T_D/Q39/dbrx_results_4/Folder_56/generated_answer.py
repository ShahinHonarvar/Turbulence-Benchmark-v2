def return_n_greatest_chars(s):
    ascii_values = sorted(list(map(ord, s)))
    n = 21
    return [chr(i) for i in ascii_values[-n:]]