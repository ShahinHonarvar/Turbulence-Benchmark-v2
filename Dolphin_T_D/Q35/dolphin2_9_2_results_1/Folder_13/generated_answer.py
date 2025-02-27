def remove_repeat_chars(s):
    freq_map = {}
    for i in range(46, 91):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    for char, freq in freq_map.items():
        if freq > 1:
            s = s.replace(char, '')
    return s