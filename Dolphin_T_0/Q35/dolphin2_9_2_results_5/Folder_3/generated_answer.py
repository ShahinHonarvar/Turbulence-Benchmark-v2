def remove_repeat_chars(s):
    char_freq = {}
    for i in range(56, 88):
        if s[i] in char_freq:
            char_freq[s[i]] += 1
        else:
            char_freq[s[i]] = 1
    repeat_chars = [k for k, v in char_freq.items() if v > 1]
    for rc in repeat_chars:
        s = s.replace(rc, '')
    return s