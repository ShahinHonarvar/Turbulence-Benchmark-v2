def filter_chars(s):
    chars_to_remove = set((ord(c) >= 63 and ord(c) <= 84 and (chr(ord(c)) >= 'E') and (chr(ord(c)) <= '~') for c in s))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))