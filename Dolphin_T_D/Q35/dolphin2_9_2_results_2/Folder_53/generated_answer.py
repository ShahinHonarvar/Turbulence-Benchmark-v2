def remove_repeat_chars(input_string):
    char_frequency = {}
    for i in range(200, 203):
        if input_string[i] not in char_frequency:
            char_frequency[input_string[i]] = 1
        else:
            char_frequency[input_string[i]] += 1
    new_string = ''
    for char in input_string:
        if char not in char_frequency or char_frequency[char] == 1:
            new_string += char
    return new_string