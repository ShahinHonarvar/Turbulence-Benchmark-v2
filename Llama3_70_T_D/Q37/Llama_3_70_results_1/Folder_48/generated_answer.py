def filter_chars(s):
    return ''.join((c for c in s if not (513 <= ord(c) <= 877 and '?' <= c <= 'n') or s.index(c) != s.rfind(c)))