def remove_repeat_chars(s):
    s = s[50:200]
    chars = {}
    for i, char in enumerate(s):
        if char in chars:
            s = s[:i] + s[i + 1:]
            for j in range(i, len(s) - 1):
                s = s[:j] + s[j + 1:]
        else:
            chars[char] = 1
    return s