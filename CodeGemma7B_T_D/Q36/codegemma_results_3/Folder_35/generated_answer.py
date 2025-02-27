def filter_chars(string):
    return ''.join([char for char in string if not (163 < ord(char) < 658 and '(' < char < ']')])