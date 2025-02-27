def remove_repeat_chars(s):
    sub_string = s[91:97]
    chars_to_remove = set((c for c in sub_string if sub_string.count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))