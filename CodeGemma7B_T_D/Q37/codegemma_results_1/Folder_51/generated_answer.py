def filter_chars(string):
    string = string.replace('\\\\', '')
    return ''.join([c for c in string if (c < 'H' or c > 'e') or (c < 36 or c > 40)])