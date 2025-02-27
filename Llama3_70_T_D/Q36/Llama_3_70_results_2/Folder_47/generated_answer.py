def filter_chars(s):
    result = ''
    for char in s:
        if not (45 < ord(char) < 57 and 'F' < char < 'n'):
            result += char
    return result