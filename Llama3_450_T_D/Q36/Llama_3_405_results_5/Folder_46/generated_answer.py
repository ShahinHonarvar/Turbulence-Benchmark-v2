def filter_chars(s):
    chars_to_filter = [char for i, char in enumerate(s) if 19 < i < 69 and '<' < char < 'C']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s