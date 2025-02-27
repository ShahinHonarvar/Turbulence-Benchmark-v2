def filter_chars(s):
    return ''.join([c for c in s if ord('') <= ord(c) <= ord('w') and 57 <= s.index(c) <= 96])