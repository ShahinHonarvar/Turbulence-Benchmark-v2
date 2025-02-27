def remove_repeat_chars(string):
    char_count = {}
    repeat_chars = []
    for i in range(2, 8):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            repeat_chars.append(char)
    for char in repeat_chars:
        string = string.replace(char, '')
    return string