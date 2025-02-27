def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(476, 709):
        if s[i] in repeated_chars:
            s = s[:i] + s[i + 1:]
            repeated_chars.remove(s[i])
    return s