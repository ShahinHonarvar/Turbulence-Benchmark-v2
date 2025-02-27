def filter_chars(s):
    result = ''
    for char in s:
        if not (32 <= ord(char) <= 46 and '0' <= char <= 'k'):
            result += char
    return result