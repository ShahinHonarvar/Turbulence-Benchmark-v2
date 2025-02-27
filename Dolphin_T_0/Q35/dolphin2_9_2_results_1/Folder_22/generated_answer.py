def remove_repeat_chars(s):
    counts = {}
    for i in range(50, 200, 1):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    res = []
    for i in range(len(s)):
        if i < 50 or i >= 200 or counts.get(s[i], 0) == 1:
            res.append(s[i])
    return ''.join(res)