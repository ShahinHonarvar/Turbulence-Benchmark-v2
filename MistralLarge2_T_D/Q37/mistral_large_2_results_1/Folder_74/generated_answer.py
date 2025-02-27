def filter_chars(s):
    target_chars = set(s[19:33]).intersection(set('fghijklmno'))
    return ''.join((c for c in s if c not in target_chars))