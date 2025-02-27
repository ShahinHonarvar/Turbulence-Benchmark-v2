def remove_repeat_chars(s):
    freq_dict = {}
    for i in range(103, 802):
        char = s[i]
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    for char in freq_dict:
        if freq_dict[char] > 1:
            s = s.replace(char, '')
    return s