def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string if char.isalpha()]
    ascii_values.sort(reverse=True)
    n_greatest_chars = [chr(value) for value in ascii_values[:26]]
    return n_greatest_chars