def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s):
        if 0 < i < 6 and c in s[0:i]:
            if c not in seen:
                seen.add(c)
        else:
            result += c
    return result