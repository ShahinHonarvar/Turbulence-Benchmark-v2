def filter_chars(s):
    result = ''
    for char in s:
        if not (51 <= ord(char) <= 96 and 'X' <= char <= 'p'):
            result += char
    return result