def filter_chars(s):
    for char in s:
        if 521 <= s.index(char) <= 722 and char >= '>' and (char <= '_'):
            s = s.replace(char, '')
    return s