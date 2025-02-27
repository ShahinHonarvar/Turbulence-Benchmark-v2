def filter_chars(s):
    new_string = ''
    for char in s:
        if (char >= '.' and char <= 'b') and (s.index(char) >= 72 and s.index(char) <= 94):
            continue
        new_string += char
    return new_string