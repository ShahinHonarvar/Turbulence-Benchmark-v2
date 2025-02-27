def remove_repeat_chars(s):
    new_s = s[:69]
    for i in range(69, 97):
        if s[i] in s[69:i] or s[i] in s[i + 1:97]:
            continue
        new_s += s[i]
    return new_s + s[97:]