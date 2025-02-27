def remove_repeat_chars(s):
    chars = set()
    for i in range(len(s)):
        if i >= 20 and i < 200 and (s[i] in chars):
            s = s[:i] + s[i + 1:]
        elif i < 200 and s[i] not in chars:
            chars.add(s[i])
    return s