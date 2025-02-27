def return_n_greatest_chars(s):
    greatest_chars = sorted(s, key=lambda x: ord(x), reverse=True)[:23]
    return sorted(greatest_chars)