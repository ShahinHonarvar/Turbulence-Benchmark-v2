def filter_chars(s):
    removal_chars = set((c for c in s[59:81] if '5' < c < '>'))
    return ''.join((c for c in s if c not in removal_chars))