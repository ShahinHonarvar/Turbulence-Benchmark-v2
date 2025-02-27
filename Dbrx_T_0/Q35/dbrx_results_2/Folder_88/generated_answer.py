def remove_repeat_chars(s):
    for char in set(s[3:9]):
        if s[3:9].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s