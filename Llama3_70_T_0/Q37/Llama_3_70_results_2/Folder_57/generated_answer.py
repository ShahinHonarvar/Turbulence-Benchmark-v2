def filter_chars(s):
    result = ''
    for char in s:
        if not (27 <= ord(char) <= 85 and '!' <= char <= 'B'):
            result += char
    return result