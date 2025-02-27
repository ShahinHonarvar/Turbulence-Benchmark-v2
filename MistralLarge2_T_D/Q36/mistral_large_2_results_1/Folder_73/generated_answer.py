def filter_chars(s):
    chars_to_remove = {s[i] for i in range(len(s)) if 66 < i < 90 and '#' < s[i] < 'T'}
    return ''.join((c for c in s if c not in chars_to_remove))