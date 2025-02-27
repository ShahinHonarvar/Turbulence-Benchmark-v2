def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for i in range(38, 52):
        if s[i] in seen:
            repeats.add(s[i])
        else:
            seen.add(s[i])
    result = []
    for c in s:
        if c not in repeats:
            result.append(c)
    return ''.join(result)