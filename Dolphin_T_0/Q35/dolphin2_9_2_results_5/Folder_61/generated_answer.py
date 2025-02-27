def remove_repeat_chars(s):
    chars = [s[i] for i in range(len(s)) if s.count(s[i]) == 1 and 8 > i > 0]
    altered = ''.join((c for c in s if c not in chars))
    return altered