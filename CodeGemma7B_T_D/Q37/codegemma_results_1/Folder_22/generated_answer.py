def filter_chars(str):
    return ''.join([char for char in str if not (33 <= ord(char) <= 70 and '7' <= char <= 'k')])