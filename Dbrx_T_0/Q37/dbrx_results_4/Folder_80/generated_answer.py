def filter_chars(s):
    filtered_chars = [char for char in s if 36 <= s.index(char) <= 79 and 'a' <= char <= 'i']
    return ''.join((char for char in s if char not in filtered_chars))