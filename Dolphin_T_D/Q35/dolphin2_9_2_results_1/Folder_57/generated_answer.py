def remove_repeat_chars(s):
    freq = [0] * 256
    for i in range(25, 80):
        freq[ord(s[i])] += 1
    for i in range(25, 80):
        if freq[ord(s[i])] > 1:
            s = s[:i] + s[i + 1:]
    return s