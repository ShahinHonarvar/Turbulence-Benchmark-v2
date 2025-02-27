def remove_repeat_chars(s):
    freq_count = {}
    for i in range(20, 93):
        char = s[i]
        if char in freq_count:
            freq_count[char] += 1
        else:
            freq_count[char] = 1
    for char, count in freq_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s