def remove_repeat_chars(string):
    repeat_chars = [char for char in string[50:92] if string.count(char) > 1]
    for char in repeat_chars:
        string = string.replace(char, '')
    return string