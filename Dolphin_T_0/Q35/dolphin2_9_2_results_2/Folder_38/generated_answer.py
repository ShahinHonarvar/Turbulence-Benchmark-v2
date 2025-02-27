def remove_repeat_chars(s):
    repeat = set()
    for i in range(36, 85):
        if s[i] in repeat:
            s = s[:i] + s[i + 1:]
            repeat.remove(s[i])
        else:
            repeat.add(s[i])
    return s