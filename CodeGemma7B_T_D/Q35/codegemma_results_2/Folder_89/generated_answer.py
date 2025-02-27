def remove_repeat_chars(string):
    repeat_chars = set()
    for i in range(55, 84):
        if string[i] in repeat_chars:
            continue
        repeat_chars.add(string[i])
        if string[i] in string[i + 1:84]:
            while string[i] in string[i + 1:84]:
                string = string[:i + 1] + string[i + 2:]
    return string