def remove_repeat_chars(s):
    counts = {}
    for i in range(27, 96):
        if i < len(s):
            counts[s[i]] = counts.get(s[i], 0) + 1
    for char in counts:
        if counts[char] > 1:
            s = s.replace(char, '')
    return s