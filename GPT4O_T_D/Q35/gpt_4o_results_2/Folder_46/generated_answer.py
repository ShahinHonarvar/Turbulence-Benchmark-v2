def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    substring = s[11:79]
    repeat_chars = {c for c in substring if substring.count(c) > 1}
    result = ''.join((c for c in s if c not in repeat_chars))
    return result