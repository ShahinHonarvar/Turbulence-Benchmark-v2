def remove_repeat_chars(string):
    unique_chars = list(set(string))
    for char in unique_chars:
        if 13 < string.index(char) < 76 and string.count(char) > 1:
            string = string.replace(char, '')
    return string