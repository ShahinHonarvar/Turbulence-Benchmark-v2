def return_n_greatest_chars(s):
    greatest_chars = sorted([char for char in s if char], key=lambda x: -ord(x))[:21]
    return sorted(greatest_chars)