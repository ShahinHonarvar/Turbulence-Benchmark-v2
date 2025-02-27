def filter_chars(s):
    for char in s[672:709]:
        if 'X' < char < '}':
            s = s.replace(char, '')
    return s