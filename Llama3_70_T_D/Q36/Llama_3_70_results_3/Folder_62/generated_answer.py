def filter_chars(s):
    chars_to_remove = set(s[63:89]).intersection({c for c in s if '*' < c < 'w'})
    return ''.join((c for c in s if c not in chars_to_remove))