def filter_chars(s):
    chars_to_remove = {s[i] for i in range(323, 526) if ')' < s[i] < 'O'}
    return ''.join((c for c in s if c not in chars_to_remove))