def filter_chars(s):
    chars_to_filter = set()
    for char in s[21:25]:
        if '5' < char < '}':
            chars_to_filter.add(char)
    return ''.join((char for char in s if char not in chars_to_filter))