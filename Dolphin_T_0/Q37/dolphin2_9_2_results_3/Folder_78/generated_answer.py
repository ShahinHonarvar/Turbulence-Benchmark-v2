def filter_chars(s):
    chars_to_filter = [char for char in s[75:100] if '8' <= char <= 'e']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s