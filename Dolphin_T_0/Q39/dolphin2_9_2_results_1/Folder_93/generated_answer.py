def return_n_greatest_chars(string):
    chars = [char for char in string]
    chars.sort(reverse=True, key=lambda c: ord(c))
    return chars[:77]