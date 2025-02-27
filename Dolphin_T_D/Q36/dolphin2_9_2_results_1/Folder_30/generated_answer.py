def filter_chars(s):
    chars_to_filter = [s[i] for i in range(23, 45) if '3' < s[i] < 'I']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s