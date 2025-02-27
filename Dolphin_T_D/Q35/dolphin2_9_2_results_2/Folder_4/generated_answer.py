def remove_repeat_chars(string):
    chars_to_remove = []
    for char in string:
        if string.count(char) > 1 and 49 <= string.index(char) <= 74:
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string