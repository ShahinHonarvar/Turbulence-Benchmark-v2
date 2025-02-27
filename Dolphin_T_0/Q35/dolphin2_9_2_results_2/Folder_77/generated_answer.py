def remove_repeat_chars(s):
    freq_map = {}
    for i in range(355, 988):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    repeat_chars = [k for k, v in freq_map.items() if v > 1]
    result = ''
    for c in s:
        if c not in repeat_chars:
            result += c
    return result