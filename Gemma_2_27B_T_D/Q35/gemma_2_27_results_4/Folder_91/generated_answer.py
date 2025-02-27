def remove_repeat_chars(s):
    seen = {}
    result = []
    for i in range(7):
        if s[i] in seen:
            seen[s[i]] += 1
        else:
            seen[s[i]] = 1
    for c in s:
        if seen.get(c, 0) == 1:
            result.append(c)
    return ''.join(result)