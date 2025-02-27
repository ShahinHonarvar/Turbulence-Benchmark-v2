def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 8):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for ch, cnt in counts.items():
        if cnt > 1:
            s = s.replace(ch, '')
    return s