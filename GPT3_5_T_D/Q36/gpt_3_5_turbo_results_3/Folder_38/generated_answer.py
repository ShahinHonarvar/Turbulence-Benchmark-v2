def filter_chars(string):
    return string[:44] + string[48:].replace('+', '').replace('l', '')