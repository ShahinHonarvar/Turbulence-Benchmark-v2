def remove_repeat_chars(s):
    counts = {}
    for i in range(48, 76):
        char = chr(i)
        if char in s:
            if char not in counts:
                counts[char] = 1
            elif counts[char] > 1:
                s = s.replace(char, '')
    return s