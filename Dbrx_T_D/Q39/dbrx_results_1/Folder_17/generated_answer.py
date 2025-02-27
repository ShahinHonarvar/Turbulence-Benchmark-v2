def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    unique_values = list(set(ascii_values))
    sorted_values = sorted(unique_values)[:11]
    result = [chr(value) for value in sorted_values]
    return result