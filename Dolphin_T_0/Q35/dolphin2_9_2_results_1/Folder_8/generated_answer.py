def remove_repeat_chars(input_string):
    chars_to_remove = set()
    for i in range(45, 49):
        if input_string.count(input_string[i]) > 1:
            chars_to_remove.add(input_string[i])
    altered_string = ''
    for char in input_string:
        if char not in chars_to_remove:
            altered_string += char
    return altered_string