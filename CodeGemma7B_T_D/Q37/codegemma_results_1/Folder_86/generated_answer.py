def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i >= 164 and i <= 706 and (ord(string[i]) >= ord('O')) and (ord(string[i]) <= ord('}')):
            continue
        result += string[i]
    return result