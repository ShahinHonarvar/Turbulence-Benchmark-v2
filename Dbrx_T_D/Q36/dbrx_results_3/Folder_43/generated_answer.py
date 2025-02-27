def filter_chars(s):
    return ''.join((c for c in s[27:75] if not 'A' < c < 'i')) + s[:27] + s[75:]