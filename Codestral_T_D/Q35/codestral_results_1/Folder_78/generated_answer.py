def remove_repeat_chars(s):
    chars = s[62:96]
    counts = {c: chars.count(c) for c in chars}
    return ''.join([c for c in s if counts[c] == 1 or c not in chars or s.index(c) < 62 or (s.index(c) > 96)])