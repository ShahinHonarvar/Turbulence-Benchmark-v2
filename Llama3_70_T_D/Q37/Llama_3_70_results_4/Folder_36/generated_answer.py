def filter_chars(s):
    result = ''
    for char in s:
        if not (259 <= ord(char) <= 502 and ',' <= char <= '3'):
            result += char
    return result