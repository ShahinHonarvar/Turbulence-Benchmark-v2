def remove_repeat_chars(s):
    repeat_chars = [c for c in s[70:98] if s[70:98].count(c) > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s