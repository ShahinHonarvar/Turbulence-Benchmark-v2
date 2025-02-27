def filter_chars(s):
    new_s = ''
    for char in s:
        if 69 <= s.index(char) <= 96 and (char > 'V' and char < 'j'):
            s = s.replace(char, '')
    return s