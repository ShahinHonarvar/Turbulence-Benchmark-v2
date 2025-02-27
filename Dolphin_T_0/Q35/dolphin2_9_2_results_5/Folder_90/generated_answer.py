def remove_repeat_chars(s):
    counts = {}
    for i in range(306, 807):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    repeat_chars = [c for c in counts if counts[c] > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s