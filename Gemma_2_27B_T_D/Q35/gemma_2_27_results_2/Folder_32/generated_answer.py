def remove_repeat_chars(s):
    counts = {}
    for i in range(86, 90):
        if s[i] not in counts:
            counts[s[i]] = 0
        counts[s[i]] += 1
    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s