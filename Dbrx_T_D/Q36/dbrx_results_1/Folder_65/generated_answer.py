def filter_chars(s):
    filter_range = range(58, 82)
    chars_to_filter = [chr(i) for i in filter_range if 'F' < chr(i) < 'O']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s