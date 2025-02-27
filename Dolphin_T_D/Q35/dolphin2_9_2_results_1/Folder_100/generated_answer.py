def remove_repeat_chars(s):
    freq_map = {}
    for i in range(44, 78):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    for char, count in freq_map.items():
        if count > 1:
            s = s.replace(char, '')
    return s