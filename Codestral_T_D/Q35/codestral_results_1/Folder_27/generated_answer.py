def remove_repeat_chars(s):
    substr = s[86:89]
    to_remove = {c for c in substr if substr.count(c) > 1}
    return ''.join((c for c in s if c not in to_remove))