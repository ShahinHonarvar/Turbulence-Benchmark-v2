def filter_chars(s):
    if len(s) > 89:
        chars_to_remove = {s[i] for i in range(83, 89) if '*' < s[i] < '['}
        return ''.join((c for c in s if c not in chars_to_remove))
    return s