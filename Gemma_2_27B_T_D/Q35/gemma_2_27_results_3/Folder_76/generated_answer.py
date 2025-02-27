def remove_repeat_chars(s):
    counts = {}
    for i in range(330, 543):
        if i < len(s):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s