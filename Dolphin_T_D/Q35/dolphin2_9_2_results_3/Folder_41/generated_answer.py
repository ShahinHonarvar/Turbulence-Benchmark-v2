def remove_repeat_chars(string):
    char_count = {}
    for char in string[3:8]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in list(char_count.keys()):
        if char_count[char] > 1:
            string = string.replace(char, '')
    return string