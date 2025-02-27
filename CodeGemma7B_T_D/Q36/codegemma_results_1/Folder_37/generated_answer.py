def filter_chars(x):
    return ''.join([i for i in x if ord(i) <= 47 or ord(i) >= 58]).strip()