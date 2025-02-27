def remove_repeat_chars(s):
    counts = {}
    for i in range(44, 78):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    repeat_chars = [k for k, v in counts.items() if v > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s