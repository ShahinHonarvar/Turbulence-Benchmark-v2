def remove_repeat_chars(s):
    counts = {}
    for i in range(2, 8):
        char = s[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char in counts:
        if counts[char] > 1:
            s = s.replace(char, '')
    return s