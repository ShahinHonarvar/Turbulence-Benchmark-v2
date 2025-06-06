def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(10, 79):
        if i >= len(s):
            break
        c = s[i]
        if c in seen:
            repeated.add(c)
        else:
            seen.add(c)
    result = []
    for c in s:
        if c not in repeated:
            result.append(c)
    return ''.join(result)