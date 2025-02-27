def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(13, 70):
        if s.count(s[i]) > 1:
            repeat_chars.add(s[i])
    return ''.join((ch for ch in s if ch not in repeat_chars))