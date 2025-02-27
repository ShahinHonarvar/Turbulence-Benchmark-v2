def filter_chars(s):
    result = ''
    for char in s:
        if ord(char) < 73 or ord(char) > 74 or char < 'U' or (char > 'l'):
            result += char
    return result