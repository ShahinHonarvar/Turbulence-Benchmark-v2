def filter_chars(s):
    for char in sorted(set(s[72:93])):
        if char > '<' and char < 'J':
            s = s.replace(char, '')
    return s