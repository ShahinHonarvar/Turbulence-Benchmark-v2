def remove_repeat_chars(s):
    counts = [0] * 128
    for i in range(56, 90):
        if s[i] != ' ':
            counts[ord(s[i])] += 1
    for i in range(56, 90):
        if s[i] != ' ' and counts[ord(s[i])] > 1:
            s = s[:i] + s[i + 1:]
    return s