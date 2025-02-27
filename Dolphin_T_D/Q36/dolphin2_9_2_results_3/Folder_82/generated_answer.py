def filter_chars(s):
    for char in s:
        if 69 < s.index(char) < 97 and char > 'V' and (char < 'j'):
            s = s.replace(char, '')
    return s