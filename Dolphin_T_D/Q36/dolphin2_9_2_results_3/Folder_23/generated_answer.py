def filter_chars(string):
    chars_to_filter = [string[i] for i in range(21, 25)]
    for char in chars_to_filter:
        if '5' < char < '}':
            string = ''.join([c for c in string if c != char])
    return string