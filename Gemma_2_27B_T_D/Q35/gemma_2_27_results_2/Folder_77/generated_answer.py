def remove_repeat_chars(s):
    counts = {}
    for i in range(355, 988):
        c = s[i]
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    for c, count in counts.items():
        if count > 1:
            s = s.replace(c, '')
    return s