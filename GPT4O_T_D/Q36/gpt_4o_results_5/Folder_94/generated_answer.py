def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('I') + 1, ord('M'))}
    affected_chars = set(s[16:85])
    chars_to_remove = to_remove.intersection(affected_chars)
    return ''.join((c for c in s if c not in chars_to_remove))