def remove_repeat_chars(s):
    char_freq = {}
    for i in range(125, 825):
        if s[i] not in char_freq:
            char_freq[s[i]] = 1
        else:
            char_freq[s[i]] += 1
    for char, freq in char_freq.items():
        if freq > 1:
            s = s.replace(char, '')
    return s