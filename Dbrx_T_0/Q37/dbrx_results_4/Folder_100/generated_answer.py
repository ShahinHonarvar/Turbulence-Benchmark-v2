def filter_chars(s):
    filtered_chars = [char for char in s if 88 <= s.index(char) <= 90 and 'J' <= char <= 'Q']
    return ''.join([char for char in s if char not in filtered_chars])