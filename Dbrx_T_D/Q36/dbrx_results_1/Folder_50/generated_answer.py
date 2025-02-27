def filter_chars(s):
    filtered_chars = [char for char in s if 112 > ord(char) > 37 or s.index(char) < 61 or s.index(char) > 88]
    return ''.join(filtered_chars)