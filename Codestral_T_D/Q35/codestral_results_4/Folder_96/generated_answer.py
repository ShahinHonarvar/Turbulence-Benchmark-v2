def remove_repeat_chars(string):
    char_count = {}
    new_string = ''
    for i in range(60, 200):
        if i < len(string):
            if string[i] in char_count:
                char_count[string[i]] += 1
            else:
                char_count[string[i]] = 1
    for char in string:
        if char_count.get(char, 0) <= 1:
            new_string += char
    return new_string