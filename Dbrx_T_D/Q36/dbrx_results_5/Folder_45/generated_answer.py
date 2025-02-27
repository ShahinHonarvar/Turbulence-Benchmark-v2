def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 81 or i >= 86 or (s[i] > '!' and s[i] < 's')))