def filter_chars(s):
    for char in s[20:70]:
        if char > '<' and char < 'C':
            s = s.replace(char, '')
    return s