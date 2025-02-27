def remove_repeat_chars(s):
    freq = [0] * 128
    for i in range(27, 97):
        c = s[i]
        freq[ord(c)] += 1
    new_s = ''
    for c in s:
        if freq[ord(c)] < 2:
            new_s += c
    return new_s