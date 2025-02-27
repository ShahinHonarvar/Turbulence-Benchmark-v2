def remove_repeat_chars(s):
    for char in set(s[57:84]):
        if s[57:84].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s