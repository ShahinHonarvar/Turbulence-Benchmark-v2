def remove_repeat_chars(s):
    chars_to_remove = {s[i] for i in range(3, 9) if s.count(s[i]) > 1}
    s_without_repeats = ''.join((c for c in s if c not in chars_to_remove))
    return s_without_repeats