def remove_repeat_chars(string):
    chars_to_remove = set()
    for i in range(62, 96):
        if chr(i) in string[62:96]:
            chars_to_remove.add(chr(i))
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string