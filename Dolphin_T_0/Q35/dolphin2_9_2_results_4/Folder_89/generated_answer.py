def remove_repeat_chars(s):
    freq_map = {}
    for i in range(55, 85):
        char = s[i]
        if char not in freq_map:
            freq_map[char] = 1
        else:
            freq_map[char] += 1
    chars_to_remove = [k for k, v in freq_map.items() if v > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s