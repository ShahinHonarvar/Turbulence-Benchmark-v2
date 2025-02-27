def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for i in range(27, 96):
        if i < len(s):
            c = s[i]
            if c in seen:
                repeats.add(c)
            else:
                seen.add(c)
    result = []
    for c in s:
        if c not in repeats:
            result.append(c)
    return ''.join(result)