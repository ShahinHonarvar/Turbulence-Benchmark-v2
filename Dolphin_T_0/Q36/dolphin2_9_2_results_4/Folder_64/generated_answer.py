def filter_chars(string):
    chars = [string[i] for i in range(1, 7) if string[i] > '3' and string[i] < '^']
    return ''.join([c for c in string if c not in chars])