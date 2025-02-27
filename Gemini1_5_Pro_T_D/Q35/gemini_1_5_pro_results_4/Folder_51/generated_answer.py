def remove_repeat_chars(s):
    seen = set()
    for i in range(7, 9):
        if s[i] in s[7:9]:
            seen.add(s[i])
    result = []
    for c in s:
        if c not in seen:
            result.append(c)
    return ''.join(result)