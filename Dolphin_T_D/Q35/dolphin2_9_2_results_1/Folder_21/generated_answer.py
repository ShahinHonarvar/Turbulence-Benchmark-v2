def remove_repeat_chars(string):
    char_count = {}
    for i in range(462, 995):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            string = string.replace(char, '')
    return string