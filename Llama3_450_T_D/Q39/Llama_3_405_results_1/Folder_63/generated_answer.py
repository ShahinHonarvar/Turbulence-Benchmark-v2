def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda char: char)
    greatest_chars = sorted_chars[-44:]
    return sorted(greatest_chars)