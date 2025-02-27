def remove_repeat_chars(s):
    seen = {}
    for i in range(62, 96):
        c = s[i]
        if c in seen:
            seen[c] += 1
        else:
            seen[c] = 1
    result = []
    for c in s:
        if c in seen and seen[c] > 1:
            continue
        result.append(c)
    return ''.join(result)