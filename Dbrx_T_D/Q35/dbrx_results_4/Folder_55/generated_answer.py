def remove_repeat_chars(s):
    for char in set(s[10:100]):
        if s[10:100].count(char) > 1:
            s = ''.join((c for c in s if c != char))
    return s