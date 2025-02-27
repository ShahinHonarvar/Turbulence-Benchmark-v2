def remove_repeat_chars(s):
    for i in range(87, 90):
        if s[i] in s[87:i] + s[i + 1:90]:
            s = s.replace(s[i], '')
    return s