def filter_chars(s):
    chars_to_remove = set(range(ord('-'), ord('D') + 1) & set(range(ord(s[770]), ord(s[969]) + 1)))
    return ''.join((c for c in s if c < '-' or c > 'D' or ord(s[770]) > ord(c) > ord(s[969]) or (c not in chars_to_remove)))