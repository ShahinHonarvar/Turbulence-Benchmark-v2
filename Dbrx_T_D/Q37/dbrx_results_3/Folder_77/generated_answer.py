def filter_chars(s):
    filtered_chars = [char for char in s if s.index(char) < 384 or s.index(char) > 411 or ord(char) < 47 or (ord(char) > 56)]
    return ''.join(filtered_chars)