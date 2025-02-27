def filter_chars(string):
    return ''.join((char for char in string if 0 <= ord(char) - ord('O') <= 34))