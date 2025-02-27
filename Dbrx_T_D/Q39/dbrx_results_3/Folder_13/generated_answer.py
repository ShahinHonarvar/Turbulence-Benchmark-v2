def return_n_greatest_chars(string):
    chars = [char for char in string if char != ' ']
    chars.sort(key=lambda char: ord(char), reverse=True)
    return chars[:31]