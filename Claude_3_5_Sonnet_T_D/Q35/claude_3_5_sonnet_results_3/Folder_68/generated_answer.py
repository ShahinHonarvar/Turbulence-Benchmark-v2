def remove_repeat_chars(s):
    substr = s[1:9]
    chars_to_remove = set((c for c in substr if substr.count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))