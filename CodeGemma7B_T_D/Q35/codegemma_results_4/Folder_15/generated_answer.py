def remove_repeat_chars(string):
    i = 0
    while i < len(string) and i < 5:
        ch = string[i]
        if string.count(ch) > 1:
            string = string.replace(ch, '', string.count(ch) - 1)
        i += 1
    return string