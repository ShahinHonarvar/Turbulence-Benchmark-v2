def remove_repeat_chars(s):
    counts = {}
    for i in range(13, 76):
        c = s[i]
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    result = []
    for c in s:
        if c not in counts or counts[c] == 1:
            result.append(c)
    return ''.join(result)