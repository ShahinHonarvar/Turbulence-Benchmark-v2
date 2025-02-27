def remove_repeat_chars(s):
    char_frequency = {}
    for char in s[19:32]:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    for char in list(char_frequency.keys()):
        if char_frequency[char] > 1:
            s = s.replace(char, '')
    return s