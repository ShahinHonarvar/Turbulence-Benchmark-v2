def filter_chars(str):
    return ''.join([c for c in str if not (90 >= ord(c) >= 19 and ord(c) >= ord('F') and (ord(c) <= ord('h')))])