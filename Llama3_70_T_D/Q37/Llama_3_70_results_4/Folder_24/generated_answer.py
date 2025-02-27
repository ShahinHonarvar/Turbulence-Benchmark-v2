def filter_chars(s):
    result = ''
    for char in s:
        if 36 <= ord(char) <= 79 and '2' <= char <= 's':
            result = result.replace(char, '')
        else:
            result += char
    return result