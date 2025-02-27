def return_n_greatest_chars(string):
    ascii_chars = [ord(char) for char in string if char != ' ']
    sorted_ascii_chars = sorted(ascii_chars, reverse=True)[:70]
    return [chr(char) for char in sorted_ascii_chars]