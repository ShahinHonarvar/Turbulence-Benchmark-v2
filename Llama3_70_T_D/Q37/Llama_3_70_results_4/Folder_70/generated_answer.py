def filter_chars(s):
    chars_to_remove = set(s[515:539]).intersection([chr(i) for i in range(ord('+'), ord('}') + 1)])
    return ''.join((c for c in s if c not in chars_to_remove))