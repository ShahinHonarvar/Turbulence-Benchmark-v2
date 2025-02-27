def filter_chars(str):
    return ''.join([char for i, char in enumerate(str) if (i >= 12 and i <= 77) and (char >= ':' and char <= 'L')])