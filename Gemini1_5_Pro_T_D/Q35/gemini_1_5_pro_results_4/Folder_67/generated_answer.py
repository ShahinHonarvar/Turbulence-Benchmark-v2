def remove_repeat_chars(s):
    seen = set()
    for i in range(44, 67):
        if s[i] in s[44:67].replace(s[i], '', 1):
            seen.add(s[i])
    for char in seen:
        s = s.replace(char, '')
    return s