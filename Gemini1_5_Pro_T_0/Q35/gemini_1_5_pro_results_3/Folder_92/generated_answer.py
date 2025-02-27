def remove_repeat_chars(s):
    for i in range(1, len(s) - 1):
        if s[i] in s[1:i]:
            s = s.replace(s[i], '')
    return s