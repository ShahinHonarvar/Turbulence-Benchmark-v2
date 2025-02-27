def return_n_greatest_chars(string):
    ascii_chars = [ord(char) for char in string if char != ' ']
    sorted_chars = sorted(ascii_chars, reverse=True)[:77]
    return [chr(char) for char in sorted_chars]