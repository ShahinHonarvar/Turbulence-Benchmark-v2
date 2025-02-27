def remove_repeat_chars(string):
    count = {}
    for i in range(57, 85):
        if string[i] in count:
            count[string[i]] += 1
        else:
            count[string[i]] = 1
    for char, value in count.items():
        if value > 1:
            string = string.replace(char, '')
    return string