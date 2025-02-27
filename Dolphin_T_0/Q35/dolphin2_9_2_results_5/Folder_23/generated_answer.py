def remove_repeat_chars(input_string):
    chars_count = {}
    for char in input_string[20:36]:
        if char not in chars_count:
            chars_count[char] = 1
        else:
            chars_count[char] += 1
    for char_index in range(len(input_string)):
        char = input_string[char_index]
        if chars_count.get(char, 0) > 1 and char_index >= 20 and (char_index < 36):
            input_string = input_string.replace(char, '')
    return input_string