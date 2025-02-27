def return_n_greatest_chars(string):
    chars = [char for char in string]
    chars.sort(key=lambda c: ord(c), reverse=True)
    return chars[:21]