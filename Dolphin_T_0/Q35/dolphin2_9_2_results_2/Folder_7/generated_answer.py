def remove_repeat_chars(string):
    char_indices = {}
    for i in range(375, 926):
        if string[i] in char_indices:
            char_indices[string[i]].append(i)
        else:
            char_indices[string[i]] = [i]
    for char in char_indices:
        if len(char_indices[char]) > 1:
            for index in char_indices[char]:
                string = string[:index] + string[index + 1:]
    return string