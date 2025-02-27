def filter_chars(s):
    result = ''
    undesirable_chars = [c for c in s[19:93] if '8' <= c <= 'm']
    for c in s:
        if c not in undesirable_chars:
            result += c
    return result