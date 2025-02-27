def filter_chars(s):
    for i in range(669, 889):
        if i < len(s):
            char = s[i]
            if char > 'B' and char < 'Y':
                s = ''.join([c for c in s if c != char])
    return s