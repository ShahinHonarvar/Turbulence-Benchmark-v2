def remove_repeat_chars(string):
    chars_to_remove = {}
    for i in range(38, 52):
        if string[i] not in chars_to_remove:
            chars_to_remove[string[i]] = 1
        else:
            chars_to_remove[string[i]] += 1
    for char, count in chars_to_remove.items():
        if count > 1:
            string = string.replace(char, '')
    return string