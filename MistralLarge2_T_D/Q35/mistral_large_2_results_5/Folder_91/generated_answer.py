def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 6):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    return ''.join([char for char in s if counts.get(char, 0) < 2])