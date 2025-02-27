def remove_repeat_chars(s):
    counts = {}
    for i in range(10, 80):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for c in counts:
        if counts[c] > 1:
            s = s.replace(c, '')
    return s