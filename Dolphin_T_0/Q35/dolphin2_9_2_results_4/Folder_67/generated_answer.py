def remove_repeat_chars(string):
    count = {}
    for i in range(44, 67):
        if string[i] not in count:
            count[string[i]] = 1
        else:
            count[string[i]] += 1
    for key, value in count.items():
        if value > 1:
            string = string.replace(key, '')
    return string