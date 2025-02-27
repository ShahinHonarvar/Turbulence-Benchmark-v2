def remove_repeat_chars(s):
    s = s[:45] + s[45:48] + s[48:]
    chars = set([c for c in s if s.count(c) > 1 and 45 < s.index(c) < 48])
    for c in chars:
        s = s.replace(c, '')
    return s