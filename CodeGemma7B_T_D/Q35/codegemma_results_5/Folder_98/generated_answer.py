def remove_repeat_chars(str):
    for i in range(8):
        char = str[i]
        while str.count(char) > 1:
            str = str.replace(char, '', str.count(char) - 1)
    return str