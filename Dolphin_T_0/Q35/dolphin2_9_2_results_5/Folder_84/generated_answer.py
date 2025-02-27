def remove_repeat_chars(s):
    freq_map = {}
    for i in range(32, 44):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    for key, value in freq_map.items():
        if value > 1:
            s = s.replace(key, '')
    return s