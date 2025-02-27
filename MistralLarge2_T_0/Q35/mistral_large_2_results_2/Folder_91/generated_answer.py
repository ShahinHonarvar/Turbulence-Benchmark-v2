def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 7):
        char = s[i]
        counts[char] = counts.get(char, 0) + 1
    for char in counts:
        if counts[char] > 1:
            s = s.replace(char, '')
    return s