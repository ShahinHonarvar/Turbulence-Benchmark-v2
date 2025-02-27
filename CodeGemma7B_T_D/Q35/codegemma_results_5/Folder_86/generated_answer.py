def remove_repeat_chars(string):
    consumed = set(string)
    for i in range(19, 32):
        if string[i] in consumed and string[i] in string[i + 1:]:
            string = string.replace(string[i], '')
            consumed.remove(string[i])
    return string