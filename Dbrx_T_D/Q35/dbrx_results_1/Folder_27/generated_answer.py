def remove_repeat_chars(s):
    for i in range(86, 89):
        if i < len(s) and s[i] in s[i + 1:]:
            s = s[:i] + s[i + 1:]
    return s