def remove_repeat_chars(s):
    substring = s[58:85]
    repeated_chars = {c for c in substring if substring.count(c) > 1}
    result = ''.join((c for c in s if c not in repeated_chars or c not in s[58:85]))
    return result