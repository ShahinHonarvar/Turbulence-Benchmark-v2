def remove_repeat_chars(s):
    target_substr = s[3:7]
    repeated_chars = set((c for c in target_substr if target_substr.count(c) > 1))
    return ''.join((c for c in s if c not in repeated_chars))