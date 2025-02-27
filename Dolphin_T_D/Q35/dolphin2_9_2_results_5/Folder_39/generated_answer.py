def remove_repeat_chars(string):
    count_chars = {}
    for i in range(44, 91):
        if string[i] not in count_chars:
            count_chars[string[i]] = 1
        else:
            count_chars[string[i]] += 1
    for char in count_chars:
        if count_chars[char] > 1:
            string = string.replace(char, '')
    return string