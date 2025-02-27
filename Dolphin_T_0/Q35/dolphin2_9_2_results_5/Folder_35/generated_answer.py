def remove_repeat_chars(s):
    counts = {}
    for i in range(77, 84):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for k, v in counts.items():
        if v > 1:
            s = s.replace(k, '')
    return s