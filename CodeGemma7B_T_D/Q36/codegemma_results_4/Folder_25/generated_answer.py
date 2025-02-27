def filter_chars(string):
    return ''.join([ch for ch in string if not (24 <= ord(ch) <= 37 and ord(ch) > ord('A') and (ord(ch) < ord('h')))])