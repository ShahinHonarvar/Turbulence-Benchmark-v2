def remove_repeat_chars(input_str):
    char_freq = {}
    for i in range(57, 85):
        char = input_str[i]
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    for char, freq in char_freq.items():
        if freq > 1:
            input_str = input_str.replace(char, '')
    return input_str