def remove_repeat_chars(s):
    char_freq = {}
    for i in range(56, 90):
        char = s[i]
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    repeat_chars = [char for char, freq in char_freq.items() if freq > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s