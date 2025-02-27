def remove_repeat_chars(s):
    for char in set(s[2:5]):
        if s[2:5].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s