def remove_repeat_chars(s):
    counts = {}
    for i in range(3, 8):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s