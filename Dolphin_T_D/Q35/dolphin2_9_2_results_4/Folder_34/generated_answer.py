def remove_repeat_chars(string):
    freq_map = {}
    for i in range(70, 200):
        if string[i] in freq_map:
            freq_map[string[i]] += 1
        else:
            freq_map[string[i]] = 1
    for key, value in freq_map.items():
        if value > 1:
            string = string.replace(key, '')
    return string