def remove_repeat_chars(s):
    for i in range(90, 200):
        for char in s[i:i + 2]:
            if char in s[i + 2:]:
                continue
            if char in s[i - 2:i]:
                continue
            s = s[:i] + char + s[i + 1:]
    return s