def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 93):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for key in counts:
        if counts[key] > 1:
            s = s.replace(key, '')
    return s