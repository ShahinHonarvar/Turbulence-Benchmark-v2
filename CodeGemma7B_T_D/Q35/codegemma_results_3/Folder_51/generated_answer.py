def remove_repeat_chars(s):
    i = 6
    while i < 9 and i < len(s):
        if s[i] in s[i + 1:9] and s[i] != s[i - 1]:
            i += 1
        elif s[i] in s[i + 2:9] and s[i] in s[i + 1]:
            i += 2
        else:
            i += 1
        if s[i] in s[i + 1:9]:
            s = s[:i] + s[i + 1:]
        elif s[i] in s[i + 2:9] and s[i] in s[i + 1]:
            s = s[:i] + s[i + 2:]
        else:
            i += 1
    return s