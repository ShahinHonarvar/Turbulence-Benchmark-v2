def filter_chars(s):
    to_remove = [char for char in s[24:83] if '5' <= char <= '<']
    return ''.join([char for char in s if char not in to_remove])