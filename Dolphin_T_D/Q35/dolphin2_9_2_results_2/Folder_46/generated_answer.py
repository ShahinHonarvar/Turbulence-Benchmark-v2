def remove_repeat_chars(s):
    counts = {}
    for i in range(10, 79):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    to_remove = [k for k, v in counts.items() if v > 1]
    for c in to_remove:
        s = s.replace(c, '')
    return s