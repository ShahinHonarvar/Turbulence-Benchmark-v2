def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(44, 91):
        if s[i] in seen:
            repeated.add(s[i])
        else:
            seen.add(s[i])
    result = []
    for c in s:
        if c not in repeated:
            result.append(c)
    return ''.join(result)