def remove_repeat_chars(s):
    seen = set()
    for i in range(3, 7):
        if s[i] in s[3:7] and s[i] not in seen:
            seen.add(s[i])
    for char in seen:
        s = s.replace(char, '')
    return s