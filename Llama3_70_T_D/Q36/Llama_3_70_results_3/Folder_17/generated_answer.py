def filter_chars(s):
    result = ''
    for char in s:
        if not (18 < ord(char) < 95 and 'K' < char < 'a'):
            result += char
    return result