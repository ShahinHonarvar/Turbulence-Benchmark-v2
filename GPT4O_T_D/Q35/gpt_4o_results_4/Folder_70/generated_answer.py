def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    sub_str = s[44:70]
    repeat_chars = {char for char in sub_str if sub_str.count(char) > 1}
    return ''.join((c for c in s if c not in repeat_chars or s.index(c) <= 43 or s.index(c) >= 71))