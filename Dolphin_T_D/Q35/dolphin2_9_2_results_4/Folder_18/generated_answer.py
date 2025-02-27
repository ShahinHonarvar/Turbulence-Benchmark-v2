def remove_repeat_chars(s):
    freq_dict = {}
    for i in range(56, 90):
        if s[i] in freq_dict:
            freq_dict[s[i]] += 1
        else:
            freq_dict[s[i]] = 1
    for key, value in freq_dict.items():
        if value > 1:
            s = s.replace(key, '')
    return s