def filter_chars(s):
    to_remove = {s[i] for i in range(299, 418) if '9' < s[i] < 'P'}
    return ''.join((c for c in s if c not in to_remove))