def remove_repeat_chars(string):
    chars = {}
    for i in string[3:8]:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    for i in list(chars):
        if chars[i] > 1:
            string = string.replace(i, '')
    return string