def remove_repeat_chars(s):
    counts = {}
    for i in range(50, 200):
        counts[s[i]] = counts.get(s[i], 0) + 1
    for char, count in counts.items():
        if count > 1:
            for _ in range(count - 1):
                s = s.replace(char, '', 1)
    return s