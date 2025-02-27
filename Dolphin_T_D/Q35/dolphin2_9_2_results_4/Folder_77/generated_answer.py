def remove_repeat_chars(s):
    counts = {}
    for i in range(355, 988):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for c, v in counts.items():
        if v > 1:
            s = s.replace(c, '')
    return s