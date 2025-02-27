def remove_repeat_chars(s):
    freq_map = {}
    for c in s[20:43]:
        if c not in freq_map:
            freq_map[c] = 1
        else:
            freq_map[c] += 1
    for c, count in freq_map.items():
        if count > 1:
            s = s.replace(c, '')
    return s