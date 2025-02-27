def filter_chars(s):
    idx = characters.index(')') + 1
    end = characters.index('O')
    return ''.join([c for c in s if c not in characters[idx:end]])