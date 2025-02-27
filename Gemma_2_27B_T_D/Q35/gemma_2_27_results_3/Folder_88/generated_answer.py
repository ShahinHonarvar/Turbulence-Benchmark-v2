def remove_repeat_chars(s):
    counts = {}
    for i in range(3, 9):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    new_s = ''
    for char in s:
        if char not in counts or counts[char] == 1:
            new_s += char
    return new_s