def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if i >= 12 and i <= 77 and (char >= ':') and (char <= 'L')])