def remove_repeat_chars(input_string):
    char_freq = {}
    for i in range(13, 70):
        if input_string[i] in char_freq:
            char_freq[input_string[i]] += 1
        else:
            char_freq[input_string[i]] = 1
    repeat_chars = [char for char, freq in char_freq.items() if freq > 1]
    altered_string = ''
    for i in input_string:
        if i not in repeat_chars:
            altered_string += i
    return altered_string