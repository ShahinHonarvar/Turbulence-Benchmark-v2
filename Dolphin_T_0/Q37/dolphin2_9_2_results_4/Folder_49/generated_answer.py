def filter_chars(s):
    result = ''
    for char in s:
        if not (42 <= s.index(char) <= 97 and char >= '*' and (char <= 'b')):
            result += char
    return result