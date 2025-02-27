def filter_chars(s):
    if len(s) < 75:
        return s
    check_char = [c for i, c in enumerate(s) if i >= 73 and i <= 74 and ('U' <= c <= 'l')]
    return ''.join((c for c in s if c not in check_char))