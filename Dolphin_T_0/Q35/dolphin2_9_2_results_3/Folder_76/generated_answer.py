def remove_repeat_chars(string):
    char_count = {}
    for i in range(330, 543):
        char = string[i]
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char, count in char_count.items():
        if count > 1:
            string = string.replace(char, '')
    return string