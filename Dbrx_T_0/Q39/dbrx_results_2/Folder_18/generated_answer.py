def return_n_greatest_chars(s):
    ascii_values = [ord(char) for char in s]
    sorted_ascii_values = sorted(ascii_values, reverse=True)[:52]
    result = [chr(value) for value in sorted_ascii_values]
    return result