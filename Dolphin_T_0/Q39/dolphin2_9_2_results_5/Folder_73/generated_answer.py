def return_n_greatest_chars(s):
    greatest_chars = sorted([char for char in s if char in s], key=lambda x: -ord(x))
    return greatest_chars[:80]