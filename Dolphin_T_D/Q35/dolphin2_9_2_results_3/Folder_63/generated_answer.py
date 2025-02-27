def remove_repeat_chars(s):
    counts = {}
    for i in range(81, 87):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
    for key in counts:
        if counts[key] > 1:
            s = s.replace(key, '')
    return s