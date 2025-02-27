def filter_chars(s):
    result = ''
    for char in s:
        if ord(char) < 259 or ord(char) > 502:
            result += char
        elif char < ',' or char > '3':
            result += char
    for char in range(259, 503):
        char = chr(char)
        if ',' <= char <= '3':
            result = result.replace(char, '')
    return result