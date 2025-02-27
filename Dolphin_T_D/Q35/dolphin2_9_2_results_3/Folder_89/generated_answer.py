def remove_repeat_chars(string):
    char_count = {}
    for i in range(55, 84):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    for char in char_count:
        if char_count[char] > 1:
            string = string.replace(char, '')
    return string