def remove_repeat_chars(s):
    chars = s[81:86]
    counts = {c: chars.count(c) for c in set(chars)}
    return ''.join([c for c in s if counts[c] == 1 or s.index(c) <= 81 or s.index(c) >= 86])