def remove_repeat_chars(s):
    freq_map = dict()
    for i in range(86, 90):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    for k, v in freq_map.items():
        if v > 1:
            s = s.replace(k, '')
    return s