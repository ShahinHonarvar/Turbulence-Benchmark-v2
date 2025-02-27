def filter_chars(s):
    filtered_chars = [char for char in s if 41 <= s.index(char) <= 86 and 'S' <= char <= 's']
    return ''.join(filtered_chars)