def remove_repeat_chars(s):
    for i in range(1, 5):
        if s[i] in s[1:i] + s[i + 1:5]:
            s = s.replace(s[i], '')
    return s