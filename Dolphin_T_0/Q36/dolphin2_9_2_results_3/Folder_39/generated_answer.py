def filter_chars(s):
    for char in s[43:59]:
        if char > '5' and char < 'C':
            s = ''.join([c for c in s if c != char])
    return s