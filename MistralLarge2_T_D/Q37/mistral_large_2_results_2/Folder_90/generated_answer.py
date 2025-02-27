def filter_chars(s):
    target_chars = set(s[348:853])
    result = ''.join([c for c in s if c not in target_chars or not 'J' <= c <= 'b'])
    return result