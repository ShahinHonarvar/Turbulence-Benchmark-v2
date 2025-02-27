def return_n_greatest_chars(string_of_chars):
    ascii_values = [ord(char) for char in string_of_chars]
    sorted_values = sorted(ascii_values)[:84]
    result = [chr(value) for value in sorted_values]
    return result