def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('!') + 1, ord('?'))])
    for i in range(42, 78):
        if s[i] in chars_to_remove:
            s = s[:i] + s[i + 1:]
            i -= 1
    return s