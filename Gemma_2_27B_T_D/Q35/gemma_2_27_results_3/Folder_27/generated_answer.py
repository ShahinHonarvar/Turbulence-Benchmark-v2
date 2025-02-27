def remove_repeat_chars(s):
    counts = {}
    for c in s[86:89]:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    for c in counts:
        if counts[c] > 1:
            s = s.replace(c, '')
    return s