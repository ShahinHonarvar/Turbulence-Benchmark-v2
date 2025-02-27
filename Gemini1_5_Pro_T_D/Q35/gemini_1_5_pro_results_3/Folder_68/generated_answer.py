def remove_repeat_chars(s):
    for i in range(1, 9):
        if s[i] in s[0:i] and s[i] in s[i + 1:]:
            s = s.replace(s[i], '')
    return s