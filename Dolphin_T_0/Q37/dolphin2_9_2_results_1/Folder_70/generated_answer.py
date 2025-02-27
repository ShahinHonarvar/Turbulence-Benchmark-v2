def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (515 <= i <= 538 and '+' <= c <= '}') or c not in s[515:539]))