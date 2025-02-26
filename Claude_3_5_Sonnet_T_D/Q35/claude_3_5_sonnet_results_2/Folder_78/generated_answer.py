def remove_repeat_chars(s):
    substr = s[63:96]
    repeat_chars = set((c for c in substr if substr.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))