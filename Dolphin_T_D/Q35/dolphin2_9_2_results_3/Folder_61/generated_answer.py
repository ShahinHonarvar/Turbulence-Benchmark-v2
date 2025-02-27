def remove_repeat_chars(s):
    for ch in s[:8]:
        if s.count(ch) > 1:
            s = s.replace(ch, '')
    return s