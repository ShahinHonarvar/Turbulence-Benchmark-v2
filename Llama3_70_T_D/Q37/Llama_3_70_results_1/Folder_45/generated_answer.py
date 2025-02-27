def filter_chars(s):
    chars_to_remove = set(s[72:95]).intersection(set('.' + ''.join((chr(i) for i in range(ord('.'), ord('b') + 1)))))
    return ''.join((c for c in s if c not in chars_to_remove))