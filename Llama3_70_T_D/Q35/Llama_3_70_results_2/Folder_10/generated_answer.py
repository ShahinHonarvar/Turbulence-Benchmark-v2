def remove_repeat_chars(s):
    s = list(s)
    for char in set(s[36:54]):
        if s[36:54].count(char) > 1:
            s = [c for c in s if c != char]
    return ''.join(s)