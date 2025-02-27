def remove_repeat_chars(string):
    char_count = {}
    for index, char in enumerate(string):
        if 62 < index < 96:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    for char, count in char_count.items():
        if count > 1:
            string = string.replace(char, '')
    return string