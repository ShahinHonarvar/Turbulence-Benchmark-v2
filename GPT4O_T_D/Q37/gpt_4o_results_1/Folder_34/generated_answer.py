def filter_chars(s):
    if len(s) < 54:
        return s
    chars_to_filter = {c for c in s[54:63] if ')' <= c <= '9'}
    return ''.join((c for c in s if c not in chars_to_filter))