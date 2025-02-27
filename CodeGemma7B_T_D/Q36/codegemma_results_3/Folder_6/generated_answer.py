def filter_chars(string):
    ''.join([char for char in string if not (31 < ord(char) < 70 and 'B' < char < 'v')])