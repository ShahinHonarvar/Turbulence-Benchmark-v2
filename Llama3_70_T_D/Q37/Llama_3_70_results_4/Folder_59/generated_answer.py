def filter_chars(s):
    chars_to_remove = set(s[2:4]).intersection({c for c in s if '5' <= c <= '_'})
    return ''.join([c for c in s if c not in chars_to_remove])