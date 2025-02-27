def remove_repeat_chars(s):
    chars_between_2_and_7 = s[2:7]
    repeat_chars = {c for c in chars_between_2_and_7 if s.count(c) > 1}
    s = ''.join([c for c in s if c not in repeat_chars])
    return s