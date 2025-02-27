def filter_chars(s):
    to_remove = {s[i] for i in range(45, 48) if '+' < s[i] < 'l'}
    return ''.join((c for c in s if c not in to_remove))