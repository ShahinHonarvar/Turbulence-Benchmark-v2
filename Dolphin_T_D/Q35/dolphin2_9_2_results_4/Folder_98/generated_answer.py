def remove_repeat_chars(s):
    chars = [s[i] for i in range(len(s)) if i < 8 and s.count(s[i]) > 1]
    return ''.join((c for c in s if c not in chars))