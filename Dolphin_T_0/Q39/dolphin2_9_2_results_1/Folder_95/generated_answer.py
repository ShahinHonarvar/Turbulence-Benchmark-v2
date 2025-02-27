def return_n_greatest_chars(s):
    chars = [char for char in s]
    chars.sort(reverse=True)
    return chars[:36]