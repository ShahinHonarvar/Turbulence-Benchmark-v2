def remove_repeat_chars(s):
    for i in range(40, 43):
        if s[i] in s[41:43] + s[39:i:1]:
            s = s.replace(s[i], '')
    return s