def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i >= 1 and i <= 5 and (ord(char) >= ord('$')) and (ord(char) <= ord(';')):
            continue
        result.append(char)
    return ''.join(result)