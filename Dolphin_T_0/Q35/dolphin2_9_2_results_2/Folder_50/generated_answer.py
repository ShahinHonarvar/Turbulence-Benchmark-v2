def remove_repeat_chars(s):
    to_remove = [c for c in set(s[13:76]) if s[13:76].count(c) > 1]
    res = ''.join((c for c in s if c not in to_remove))
    return res