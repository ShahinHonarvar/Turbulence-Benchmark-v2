def remove_repeat_chars(s):
    char_freqs = {}
    for i in range(44, 78):
        if s[i] in char_freqs:
            char_freqs[s[i]] += 1
        else:
            char_freqs[s[i]] = 1
    for char in char_freqs:
        if char_freqs[char] > 1:
            s = s.replace(char, '')
    return s