def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 36):
        char = s[i]
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    for char in counts:
        if counts[char] > 1:
            s = s.replace(char, '')
    return s