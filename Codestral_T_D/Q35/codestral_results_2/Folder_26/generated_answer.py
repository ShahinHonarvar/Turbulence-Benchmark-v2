def remove_repeat_chars(input_string):
    char_count = {}
    for i in range(68, 100):
        char = input_string[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    new_string = ''
    for char in input_string:
        if char_count.get(char, 0) <= 1:
            new_string += char
    return new_string