def filter_chars(s):
    filtered_chars = [char for char in s if 225 <= s.index(char) <= 381 and 'D' <= char <= 'Y']
    return ''.join(filtered_chars)