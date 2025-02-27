def remove_repeat_chars(s):
    for char in set(s[1:8]):
        if s[1:8].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s