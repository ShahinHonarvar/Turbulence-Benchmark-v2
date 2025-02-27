def filter_chars(string):
    chars_to_filter = {char for i, char in enumerate(string) if 24 <= i <= 82 and '5' <= char <= '<'}
    return ''.join((char for char in string if char not in chars_to_filter))