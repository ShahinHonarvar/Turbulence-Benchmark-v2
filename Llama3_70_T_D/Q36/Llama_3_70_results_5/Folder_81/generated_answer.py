def filter_chars(s):
    to_remove = set([s[i] for i in range(51, 76) if '5' < s[i] < 'f'])
    return ''.join([c for c in s if c not in to_remove])