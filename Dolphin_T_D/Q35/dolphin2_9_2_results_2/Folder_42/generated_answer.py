def remove_repeat_chars(s):
    freq_map = {}
    for i in range(18, 60):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    repeat_chars = {key for key, value in freq_map.items() if value > 1}
    new_s = ''
    for i in range(len(s)):
        if s[i] not in repeat_chars:
            new_s += s[i]
    return new_s