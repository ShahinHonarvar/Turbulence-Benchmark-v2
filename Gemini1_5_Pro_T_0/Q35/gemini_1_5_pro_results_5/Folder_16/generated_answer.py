def remove_repeat_chars(s):
    for i in range(91, 97):
        if s[i] in s[91:i] or s[i] in s[i + 1:97]:
            s = s.replace(s[i], '')
    return s