def remove_repeat_chars(s):
    counts = {}
    for i in range(37, 43):
        if i < len(s):
            char = s[i]
            counts[char] = counts.get(char, 0) + 1
    for char in counts:
        if counts[char] > 1:
            s = s.replace(char, '')
    return s