def filter_chars(s):
    if len(s) < 90:
        relevant_chars = s[35:]
    else:
        relevant_chars = s[35:90]
    to_remove = {c for c in relevant_chars if 'E' <= c <= 't'}
    return ''.join((c for c in s if c not in to_remove))