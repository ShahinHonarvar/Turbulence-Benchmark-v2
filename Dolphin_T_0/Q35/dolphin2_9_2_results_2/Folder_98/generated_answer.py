def remove_repeat_chars(s):
    chars = {}
    for i in range(8):
        if s[i] in chars and chars[s[i]]:
            s = s.replace(s[i], '')
            chars[s[i]] = False
    return s