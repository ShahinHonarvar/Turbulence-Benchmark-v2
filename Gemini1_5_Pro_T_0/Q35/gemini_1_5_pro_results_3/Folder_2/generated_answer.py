def remove_repeat_chars(s):
    seen = set()
    for i in range(72, 93):
        if s[i] in s[72:i] + s[i + 1:93]:
            seen.add(s[i])
    result = []
    for c in s:
        if c not in seen:
            result.append(c)
    return ''.join(result)