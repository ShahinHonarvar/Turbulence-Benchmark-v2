def remove_repeat_chars(s):
    counts = {}
    for i in range(27, 97):
        counts[chr(i)] = s[i - 26:].count(chr(i))
        if counts[chr(i)] > 1:
            s = s.replace(chr(i), '')
    return s