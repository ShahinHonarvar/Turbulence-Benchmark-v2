def filter_chars(s):
    result = ''
    for char in s:
        if not (33 <= ord(char) <= 70 and '7' <= char <= 'k'):
            result += char
    return result