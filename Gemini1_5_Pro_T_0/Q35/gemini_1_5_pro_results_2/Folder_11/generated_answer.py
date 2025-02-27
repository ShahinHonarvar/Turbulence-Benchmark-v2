def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s):
        if 48 < i < 76:
            if c in seen:
                continue
            elif s[48:76].count(c) > 1:
                seen.add(c)
                continue
        result += c
    return result