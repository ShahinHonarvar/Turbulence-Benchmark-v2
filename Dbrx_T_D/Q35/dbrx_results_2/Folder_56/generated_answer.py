def remove_repeat_chars(s):
    chars_between_7_9 = set(s[7:9])
    repeat_chars = {c for c in chars_between_7_9 if s[:7].count(c) + s[9:].count(c) > 0}
    for c in repeat_chars:
        s = s.replace(c, '')
    return s