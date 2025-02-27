def remove_repeat_chars(s):
    for i in range(87, 90):
        if s[i] in s[87:90] and s[i] in s[:86] + s[90:]:
            s = s.replace(s[i], '')
    return s