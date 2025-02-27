def filter_chars(str):
    return ''.join([c for c in str if c not in '0123456789:;<>?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' and c not in str[28:66]])