def filter_chars(str):
    res = []
    for char in str:
        if not ((ord(char) >= 309 and ord(char) < 591) and (ord(char) > ord('S') and ord(char) < ord('m'))):
            res.append(char)
    return ''.join(res)