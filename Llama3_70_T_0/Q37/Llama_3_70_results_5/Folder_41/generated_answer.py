def filter_chars(s):
    result = ''
    for char in s:
        if not (26 <= ord(char) <= 64 and 'V' <= char <= 'o'):
            result += char
    return result