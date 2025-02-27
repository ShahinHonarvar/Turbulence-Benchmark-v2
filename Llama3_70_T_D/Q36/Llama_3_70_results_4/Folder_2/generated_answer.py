def filter_chars(s):
    result = ''
    for char in s:
        if ord(char) < ord('D') or ord(char) > ord('J') or s.index(char) < 421 or (s.index(char) > 854):
            result += char
    return result