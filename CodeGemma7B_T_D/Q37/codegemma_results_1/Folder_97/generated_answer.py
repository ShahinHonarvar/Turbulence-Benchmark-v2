from string import ascii_uppercase, ascii_lowercase

def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if i in range(227, 236) and c in ascii_uppercase + ascii_lowercase + 'D' + 'u':
            continue
        res += c
    return res