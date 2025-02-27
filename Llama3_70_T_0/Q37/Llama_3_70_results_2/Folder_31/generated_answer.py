def filter_chars(s):
    result = ''
    for char in s:
        if not (57 <= ord(char) <= 96 and char >= '<' and (char <= 'w')):
            result += char
    return result