def remove_repeat_chars(s):
    freq_map = {}
    for i in range(1, 9):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    for key in freq_map:
        if freq_map[key] > 1:
            s = s.replace(key, '')
    return s