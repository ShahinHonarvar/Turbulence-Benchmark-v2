def remove_repeat_chars(input_str):
    char_freq = {}
    for i in range(462, 995):
        if input_str[i] in char_freq:
            char_freq[input_str[i]] += 1
        else:
            char_freq[input_str[i]] = 1
    for char, freq in char_freq.items():
        if freq > 1:
            input_str = input_str.replace(char, '')
    return input_str