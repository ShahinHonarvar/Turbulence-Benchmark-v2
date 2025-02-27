def filter_chars(s):
    return ''.join([char for char in s if 124 <= ord(char) <= 854 and char not in '9' and (char not in 's')])