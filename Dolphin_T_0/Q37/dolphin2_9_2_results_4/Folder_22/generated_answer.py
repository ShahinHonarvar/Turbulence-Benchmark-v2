def filter_chars(string):
    result = ''
    for char in string:
        if 33 <= ord(char) <= 70 and '7' <= char <= 'k':
            continue
        else:
            result += char
    return result