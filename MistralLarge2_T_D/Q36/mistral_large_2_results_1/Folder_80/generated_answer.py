def filter_chars(s):
    remove_chars = {c for c in s[54:92] if 'J' < c < 'X'}
    return ''.join((c for c in s if c not in remove_chars))