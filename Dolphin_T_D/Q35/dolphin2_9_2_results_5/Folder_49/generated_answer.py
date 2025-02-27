def remove_repeat_chars(string):
    char_freq = {}
    for i in range(90, 201):
        if string[i] in char_freq:
            char_freq[string[i]] += 1
        else:
            char_freq[string[i]] = 1
    to_remove = [char for char, freq in char_freq.items() if freq > 1]
    new_string = ''
    for i in range(len(string)):
        if i < 90 or i > 200 or string[i] not in to_remove:
            new_string += string[i]
    return new_string