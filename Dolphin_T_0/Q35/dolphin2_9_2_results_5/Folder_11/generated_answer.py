def remove_repeat_chars(string):
    repeat_chars = {}
    for i in range(48, 76):
        char = string[i]
        if char in repeat_chars:
            repeat_chars[char] += 1
        else:
            repeat_chars[char] = 1
    for char in repeat_chars:
        if repeat_chars[char] > 1:
            string = string.replace(char, '')
    return string