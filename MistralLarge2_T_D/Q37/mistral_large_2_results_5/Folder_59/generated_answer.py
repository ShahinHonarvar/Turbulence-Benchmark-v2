def filter_chars(s):
    chars_to_remove = {s[i] for i in range(2, 4) if '5' <= s[i] <= '_'}
    return ''.join((c for c in s if c not in chars_to_remove))