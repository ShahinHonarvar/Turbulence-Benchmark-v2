def remove_repeat_chars(s):
    seen = set()
    for i in range(len(s)):
        if i >= 32 and i < 44:
            if s[i] in seen:
                s = s[:i] + s[i + 1:]
                i -= 1
            else:
                seen.add(s[i])
    return s