def remove_repeat_chars(s):
    sub_str = s[1:10]
    repeated_chars = set((ch for ch in sub_str if sub_str.count(ch) > 1))
    return ''.join((ch for ch in s if ch not in repeated_chars))