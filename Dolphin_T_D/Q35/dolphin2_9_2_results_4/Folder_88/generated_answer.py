def remove_repeat_chars(input_string):
    repeat_chars = set()
    for i in range(3, 9):
        if input_string.count(input_string[i]) > 1:
            repeat_chars.add(input_string[i])
    new_string = ''
    for i in range(len(input_string)):
        if input_string[i] not in repeat_chars:
            new_string += input_string[i]
    return new_string