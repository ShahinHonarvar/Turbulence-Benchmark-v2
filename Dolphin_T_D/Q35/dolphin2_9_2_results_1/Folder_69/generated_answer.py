def remove_repeat_chars(string):
    chars_to_remove = {}
    for i in range(39, 43):
        if string[i] in chars_to_remove:
            chars_to_remove[string[i]].append(i)
        else:
            chars_to_remove[string[i]] = [i]
    for char, indices in chars_to_remove.items():
        string = string.replace(char, '')
    return string