def remove_repeat_chars(string):
    chars = set()
    for i in range(11, 76):
        if string[i] in chars:
            string = string[:i] + string[i + 1:]
        else:
            chars.add(string[i])
    return string