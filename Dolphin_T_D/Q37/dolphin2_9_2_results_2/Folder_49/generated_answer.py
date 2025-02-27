def filter_chars(s):
    for char in s:
        if 42 <= s.index(char) <= 97 and char >= '*' and (char <= 'b'):
            s = s.replace(char, '')
    return s