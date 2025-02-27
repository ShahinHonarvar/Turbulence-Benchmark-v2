def remove_repeat_chars(s):
    frequency = {}
    for i in range(57, 85):
        if s[i] in frequency:
            frequency[s[i]] += 1
        else:
            frequency[s[i]] = 1
    for char in frequency:
        if frequency[char] > 1:
            s = s.replace(char, '')
    return s