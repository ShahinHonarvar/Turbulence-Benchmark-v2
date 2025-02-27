def filter_chars(s):
    to_remove = set(s[171:195])
    return ''.join((c for c in s if c not in to_remove or not '!' < c < '}'))