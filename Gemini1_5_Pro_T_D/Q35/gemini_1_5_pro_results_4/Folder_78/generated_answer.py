def remove_repeat_chars(s):
    for i in range(63, 96):
        if s[i] in s[63:i] + s[i + 1:96]:
            s = s.replace(s[i], '')
    return s