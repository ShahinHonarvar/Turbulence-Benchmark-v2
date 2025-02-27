def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda c: -ord(c))
    greatest_chars = sorted_chars[:17]
    return sorted(greatest_chars)