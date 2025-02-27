def filter_chars(str):
    filtered = ''
    for i in range(len(str)):
        if i >= 27 and i <= 85 and (ord(str[i]) >= ord('!')) and (ord(str[i]) <= ord('B')):
            continue
        filtered += str[i]
    return filtered