def remove_repeat_chars(s):
    counts = {}
    for i in range(36, 52):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    for char in counts:
        if counts[char] > 1:
            s = s.replace(char, '')
    return s