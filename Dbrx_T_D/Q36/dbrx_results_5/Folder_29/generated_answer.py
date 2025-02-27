def filter_chars(s):
    filtered_chars = [char for char in s if s.index(char) < 46 or s.index(char) > 68 or ord('H') < ord(char) < ord('s')]
    return ''.join(filtered_chars)