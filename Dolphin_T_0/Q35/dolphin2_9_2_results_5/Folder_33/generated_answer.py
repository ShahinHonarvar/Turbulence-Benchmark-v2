def remove_repeat_chars(s):
    counts = dict()
    for i in range(125, 825):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    repeats = []
    for char, count in counts.items():
        if count > 1:
            repeats.append(char)
    for char in repeats:
        s = s.replace(char, '')
    return s