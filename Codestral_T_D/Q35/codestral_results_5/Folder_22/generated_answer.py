def remove_repeat_chars(string):
    repeat_chars = set()
    for i in range(50, 200):
        if string.count(string[i]) > 1:
            repeat_chars.add(string[i])
    for char in repeat_chars:
        string = string.replace(char, '')
    return string