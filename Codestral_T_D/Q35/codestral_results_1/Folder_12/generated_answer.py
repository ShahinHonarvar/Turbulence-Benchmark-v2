def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(16, 87):
        if string.count(string[i]) > 1:
            repeated_chars.add(string[i])
    for char in repeated_chars:
        string = string.replace(char, '')
    return string