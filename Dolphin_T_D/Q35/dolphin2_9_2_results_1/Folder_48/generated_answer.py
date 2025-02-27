def remove_repeat_chars(s):
    counts = {}
    for i in range(409, 502):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for ch, count in counts.items():
        if count > 1:
            s = s.replace(ch, '')
    return s