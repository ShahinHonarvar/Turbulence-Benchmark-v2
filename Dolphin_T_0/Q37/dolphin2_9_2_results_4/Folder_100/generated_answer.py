def filter_chars(s):
    new_string = ''
    for char in s:
        if 88 <= ord(char) <= 90 and 'J' <= char <= 'Q':
            new_string += s.replace(char, '')
    return new_string