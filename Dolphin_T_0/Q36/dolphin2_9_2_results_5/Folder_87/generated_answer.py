def filter_chars(s):
    chars_to_filter = [chr(i) for i in range(32, 61)]
    for char in chars_to_filter:
        if '3' < char < 'D':
            s = s.replace(char, '')
    return s