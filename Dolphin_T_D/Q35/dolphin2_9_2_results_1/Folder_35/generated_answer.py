def remove_repeat_chars(s):
    char_frequency = {}
    for i in range(77, 84):
        char_frequency[s[i]] = char_frequency.get(s[i], 0) + 1
    for char in sorted(char_frequency.keys(), key=lambda x: -char_frequency[x]):
        if char_frequency[char] > 1:
            s = s.replace(char, '')
    return s