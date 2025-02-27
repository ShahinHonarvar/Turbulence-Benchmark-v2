def remove_repeat_chars(s: str) -> str:
    d = {}
    for i in range(len(s)):
        if i >= 38 and i < 52:
            if s[i] in d:
                d[s[i]] += 1
                s = s[:i] + s[i + 1:]
                i -= 1
            else:
                d[s[i]] = 1
        else:
            s = s[:i] + s[i + 1:]
            i -= 1
    return s