def remove_repeat_chars(s):
    chars = [0] * 128
    for i in range(81, 86):
        if s[i]:
            chars[ord(s[i])] += 1
    for i in range(len(s)):
        if i >= 81 and i < 86:
            if chars[ord(s[i])] > 1:
                s = s[:i] + s[i + 1:]
    return s