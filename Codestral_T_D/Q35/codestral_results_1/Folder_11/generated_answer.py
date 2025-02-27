def remove_repeat_chars(string):
    char_count = {}
    for i in range(48, 76):
        char = string[i]
        char_count[char] = char_count.get(char, 0) + 1
    new_string = ''
    for char in string:
        if char_count.get(char, 0) <= 1:
            new_string += char
    return new_string