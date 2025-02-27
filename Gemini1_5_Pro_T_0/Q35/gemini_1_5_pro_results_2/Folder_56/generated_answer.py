def remove_repeat_chars(s):
    for i in range(8, 9):
        if s[i] in s[8:9] and s[i] in s[:8] + s[9:]:
            s = s.replace(s[i], '')
    return s