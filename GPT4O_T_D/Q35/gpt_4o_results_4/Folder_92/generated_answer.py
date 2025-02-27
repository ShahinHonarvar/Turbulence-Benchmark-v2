def remove_repeat_chars(s):
    substring = s[1:2]
    to_remove = {c for c in substring if substring.count(c) > 1}
    return ''.join((c for c in s if c not in to_remove))