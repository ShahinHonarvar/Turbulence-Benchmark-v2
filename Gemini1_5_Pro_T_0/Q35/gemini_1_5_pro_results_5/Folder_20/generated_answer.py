def remove_repeat_chars(s):
    seen = set()
    for i in range(28, 96):
        if s[i] in s[28:i] or s[i] in s[i + 1:96]:
            seen.add(s[i])
    result = []
    for c in s:
        if c not in seen:
            result.append(c)
    return ''.join(result)