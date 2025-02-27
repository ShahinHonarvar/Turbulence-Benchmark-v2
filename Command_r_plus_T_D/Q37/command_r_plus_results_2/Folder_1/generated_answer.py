def filter_chars(s):
    filtered_chars = [char for char in s if not (41 <= s.index(char) <= 79 and 'f' <= char <= '|')]
    return ''.join(filtered_chars)