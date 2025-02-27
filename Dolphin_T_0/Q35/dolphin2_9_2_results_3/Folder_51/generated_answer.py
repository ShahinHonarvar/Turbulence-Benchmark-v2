def remove_repeat_chars(string):
    char_count = {}
    for c in string[6:9]:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c in list(char_count.keys()):
        if char_count[c] > 1:
            string = string.replace(c, '')
    return string