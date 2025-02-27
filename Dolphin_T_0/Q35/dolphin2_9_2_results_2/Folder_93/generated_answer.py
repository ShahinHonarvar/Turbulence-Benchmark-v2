def remove_repeat_chars(string):
    char_frequency = {}
    for i in range(57, 85):
        if string[i] in char_frequency:
            char_frequency[string[i]] += 1
        else:
            char_frequency[string[i]] = 1
    for char, freq in char_frequency.items():
        if freq > 1:
            string = string.replace(char, '')
    return string