def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 26 <= i <= 64 and 'V' <= char <= 'o':
            result += string.replace(char, '')
            break
        else:
            result += char
    return result if result else string