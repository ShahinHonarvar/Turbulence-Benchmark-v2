def remove_repeat_chars(string):
    chars = {}
    for i in range(125, 825, 1):
        if string[i] not in chars:
            chars[string[i]] = 1
        else:
            chars[string[i]] += 1
    for char in chars:
        if chars[char] > 1:
            string = string.replace(char, '')
    return string