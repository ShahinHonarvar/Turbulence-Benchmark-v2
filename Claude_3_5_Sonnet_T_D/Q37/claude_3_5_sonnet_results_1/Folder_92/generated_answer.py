def filter_chars(s):
    target_chars = set(s[4:5]).intersection(set('789:;<=>?@ABCDEFGHIJKLMNO'))
    return ''.join((c for c in s if c not in target_chars))