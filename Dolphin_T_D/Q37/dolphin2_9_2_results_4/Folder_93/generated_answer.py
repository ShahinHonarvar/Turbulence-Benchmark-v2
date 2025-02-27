def filter_chars(s):
    for char in s[38:70]:
        if 'H' <= char <= 'e':
            s = s.replace(char, '')
    return s