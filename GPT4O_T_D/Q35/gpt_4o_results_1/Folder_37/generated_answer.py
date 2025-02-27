def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    mid_substr = s[3:7]
    repeated_chars = set((c for c in mid_substr if mid_substr.count(c) > 1))
    result = ''.join((c for c in s if c not in repeated_chars))
    return result