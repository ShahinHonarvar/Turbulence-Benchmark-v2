def remove_repeat_chars(string):
    chars_to_remove = []
    for i in range(1, 11):
        if string[i] in string[:i]:
            chars_to_remove.append(string[i])
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string