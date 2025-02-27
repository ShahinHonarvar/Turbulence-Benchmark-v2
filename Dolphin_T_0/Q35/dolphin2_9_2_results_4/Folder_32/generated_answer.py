def remove_repeat_chars(string):
    chars_to_remove = [string[i] for i in range(86, 90) if string.count(string[i]) > 1]
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string