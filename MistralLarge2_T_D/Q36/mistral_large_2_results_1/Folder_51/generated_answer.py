def filter_chars(s):
    to_remove = {s[i] for i in range(58, 81) if '5' < s[i] < '>'}
    return ''.join([c for c in s if c not in to_remove])