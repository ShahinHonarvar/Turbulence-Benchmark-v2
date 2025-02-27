def return_n_greatest_chars(string):
    ascii_values = sorted((ord(c) for c in string), reverse=True)[:44]
    return ''.join((chr(c) for c in ascii_values))