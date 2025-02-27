def remove_repeat_chars(string):
    for i in range(86, 99):
        char = string[i]
        if char in string[:i] + string[i + 1:]:
            string = string.replace(char, '')
    return string