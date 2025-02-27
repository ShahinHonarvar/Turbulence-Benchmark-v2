def remove_repeat_chars(s):
    counts = {}
    for char in s[86:89]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
    return s