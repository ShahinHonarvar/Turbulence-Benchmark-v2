def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    ascii_values.sort(reverse=True)
    return [chr(value) for value in ascii_values[:55]]