def remove_repeat_chars(s):
    counts = {}
    for i in range(57, 85):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    repeat_chars = [char for char, count in counts.items() if count > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s