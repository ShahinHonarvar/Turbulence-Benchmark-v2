def remove_repeat_chars(s):
    counts = {}
    for i in range(35, 65):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for key, value in counts.items():
        if value > 1:
            s = s.replace(key, '')
    return s