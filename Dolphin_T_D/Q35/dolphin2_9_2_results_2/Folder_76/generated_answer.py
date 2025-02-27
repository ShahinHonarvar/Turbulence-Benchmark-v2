def remove_repeat_chars(string):
    char_freq = {}
    for char in string[330:543]:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    for char, freq in char_freq.items():
        if freq > 1:
            string = string.replace(char, '')
    return string