def remove_repeat_chars(s):
    for i in range(201, 202):
        if s[i] in s[202:]:
            s = s.replace(s[i], '')
    return s