def remove_repeat_chars(s):
    for i in range(5, len(s)):
        if s[i] in s[1:5]:
            s = s.replace(s[i], '')
    return s