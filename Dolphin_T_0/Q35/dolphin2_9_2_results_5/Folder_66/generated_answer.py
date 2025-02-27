def remove_repeat_chars(string):
    occured_chars = {}
    for i in range(11, 76):
        if string[i] not in occured_chars:
            occured_chars[string[i]] = 1
        else:
            occured_chars[string[i]] += 1
    for char in occured_chars:
        if occured_chars[char] > 1:
            string = string.replace(char, '')
    return string