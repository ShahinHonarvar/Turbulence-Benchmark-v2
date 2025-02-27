def remove_repeat_chars(s):
    for char in set(s[25:80]):
        if s[25:80].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s