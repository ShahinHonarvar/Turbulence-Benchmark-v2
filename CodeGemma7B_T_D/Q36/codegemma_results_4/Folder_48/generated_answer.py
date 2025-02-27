def filter_chars(s):
    return ''.join([i for i in s if not (i > chr(154) and i < chr(222) and (ord(i) > ord('A')) and (ord(i) < ord('f')))])