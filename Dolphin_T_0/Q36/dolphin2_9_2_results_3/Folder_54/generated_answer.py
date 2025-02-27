def filter_chars(s):
    char_range = s[18:38]
    for char in char_range:
        if char > ')' and char < 'P':
            s = s.replace(char, '')
    return s