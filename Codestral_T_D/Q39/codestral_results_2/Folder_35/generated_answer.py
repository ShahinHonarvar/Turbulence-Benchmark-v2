def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    greatest_chars = sorted_chars[-7:]
    return sorted(greatest_chars)