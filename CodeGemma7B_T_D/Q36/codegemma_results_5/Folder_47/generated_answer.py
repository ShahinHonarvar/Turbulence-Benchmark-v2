def filter_chars(string):
    return ''.join([i for i in string if ord(i) < 45 or ord(i) > 57 or (ord(i) > ord('F') and ord(i) < ord('n'))])