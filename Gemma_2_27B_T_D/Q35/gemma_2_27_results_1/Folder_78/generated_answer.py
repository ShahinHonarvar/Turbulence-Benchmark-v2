def remove_repeat_chars(s):
    counts = {}
    for c in s[62:96]:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    result = []
    for c in s:
        if c not in counts or counts[c] == 1:
            result.append(c)
        else:
            counts[c] -= 1
    return ''.join(result)