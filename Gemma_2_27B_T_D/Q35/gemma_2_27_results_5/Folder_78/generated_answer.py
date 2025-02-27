def remove_repeat_chars(s):
    counts = {}
    for i in range(62, 96):
        char = s[i]
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s