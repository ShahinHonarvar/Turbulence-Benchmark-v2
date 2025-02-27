def filter_chars(string):
    return string[:38] + ''.join([ch for ch in string[38:69] if ch < 'H' or ch > 'e']) + string[69:]