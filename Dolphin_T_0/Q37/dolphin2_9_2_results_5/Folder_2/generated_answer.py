def filter_chars(s):
    to_remove = [c for c in s[477:985] if ',' <= c <= 'V']
    result = ''
    for c in s:
        if c not in to_remove:
            result += c
    return result