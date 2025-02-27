def remove_repeat_chars(s):
    counts = {}
    for i in range(27, 96):
        if s[i] not in counts:
            counts[s[i]] = 0
        counts[s[i]] += 1
    res = ''
    for c in s:
        if counts.get(c, 0) < 2:
            res += c
    return res