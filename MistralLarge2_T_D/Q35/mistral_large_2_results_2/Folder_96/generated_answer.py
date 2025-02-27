def remove_repeat_chars(s):
    counts = {}
    for i in range(60, 200):
        if i < len(s):
            char = s[i]
            counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s