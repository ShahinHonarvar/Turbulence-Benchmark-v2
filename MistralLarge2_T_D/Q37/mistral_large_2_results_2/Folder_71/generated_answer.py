def filter_chars(s):
    removal_set = set(s[32:47]) & set('0123456789abcdefghijk')
    return ''.join((c for c in s if c not in removal_set))