def remove_repeat_chars(s):
    chars = {}
    for i in range(73, 84, 1):
        if s[i] not in chars and s.count(s[i]) > 1:
            chars[s[i]] = 1
    for i in range(0, 73, 1):
        chars[s[i]] = 0
    for i in range(84, len(s), 1):
        chars[s[i]] = 0
    for i in range(73, 84, 1):
        if s[i] not in chars:
            s = s[:73] + s[i] + s[74:i] + s[i + 1:84]
    return s