def remove_repeat_chars(string):
    chars_to_remove = []
    for i in range(330, 543):
        if string[i] in string[i + 1:543]:
            chars_to_remove.append(string[i])
    for char in set(chars_to_remove):
        string = string.replace(char, '')
    return string