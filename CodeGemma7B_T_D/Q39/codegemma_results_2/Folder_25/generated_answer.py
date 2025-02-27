def return_n_greatest_chars(string):
    ascii_values = sorted([ord(char) for char in string], reverse=True)
    return ''.join((chr(value) for value in ascii_values[:29]))