def filter_chars(string):
    return ''.join([ch for ch in string if ord(ch) not in range(ord('w'), ord('{') + 1) or ch == string[23]])