def remove_repeat_chars(s):
    char_freq = {}
    for char in s[44:91]:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    for char in set(char_freq):
        if char_freq[char] > 1:
            s = s.replace(char, '')
    return s