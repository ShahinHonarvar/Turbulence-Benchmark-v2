def remove_repeat_chars(s):
    freq_map = {}
    for i in range(13, 91):
        if s[i] in freq_map:
            freq_map[s[i]] += 1
        else:
            freq_map[s[i]] = 1
    repeats = [k for k, v in freq_map.items() if v > 1]
    result = ''
    for i in range(len(s)):
        if s[i] not in repeats:
            result += s[i]
    return result