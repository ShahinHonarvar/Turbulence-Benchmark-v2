def remove_repeat_chars(input_string):
    char_freq = {}
    for i in range(20, 51):
        if input_string[i] in char_freq:
            char_freq[input_string[i]] += 1
        else:
            char_freq[input_string[i]] = 1
    for char, freq in char_freq.items():
        if freq > 1:
            input_string = input_string.replace(char, '')
    return input_string