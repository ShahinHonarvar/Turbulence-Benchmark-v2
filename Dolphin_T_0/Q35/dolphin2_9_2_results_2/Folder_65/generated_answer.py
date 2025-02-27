def remove_repeat_chars(s):
    freq_map = {}
    for i in range(51, 76):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    to_remove = [k for k, v in freq_map.items() if v > 1]
    for char in to_remove:
        s = s.replace(char, '')
    return s