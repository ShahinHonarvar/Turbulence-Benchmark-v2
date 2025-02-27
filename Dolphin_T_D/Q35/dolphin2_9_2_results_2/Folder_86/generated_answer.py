def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 33):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    res = ''
    for c in s:
        if counts.get(c, 0) == 1:
            res += c
        else:
            res += ''
    return res