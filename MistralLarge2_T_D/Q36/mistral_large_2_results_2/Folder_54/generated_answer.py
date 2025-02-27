def filter_chars(s):
    exclusion_set = {s[i] for i in range(18, 38) if ')' < s[i] < 'P'}
    return ''.join((c for c in s if c not in exclusion_set))