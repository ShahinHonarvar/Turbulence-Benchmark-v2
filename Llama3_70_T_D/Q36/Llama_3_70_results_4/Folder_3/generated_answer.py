def filter_chars(s):
    charsToRemove = set(s[42:78].split('!')[-1].split('?')[0])
    return ''.join([c for c in s if c not in charsToRemove])