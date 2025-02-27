def filter_chars(s):
    to_remove = set(s[46:86]).intersection([chr(i) for i in range(ord('-'), ord('X') + 1)])
    return ''.join([c for c in s if c not in to_remove])