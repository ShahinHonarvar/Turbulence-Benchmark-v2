def remove_repeat_chars(s):
    for char in set(s[22:24]):
        if s[22:24].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s