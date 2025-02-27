def return_n_greatest_chars(string):
    chars = []
    for char in string:
        ascii_val = ord(char)
        if ascii_val < 128:
            chars.append(char)
    chars.sort(reverse=True)
    return chars[:61]