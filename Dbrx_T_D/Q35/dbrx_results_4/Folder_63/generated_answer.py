def remove_repeat_chars(s):
    substring = s[81:86]
    chars = set(substring)
    result = ''.join((c for c in s if c in chars))
    return result