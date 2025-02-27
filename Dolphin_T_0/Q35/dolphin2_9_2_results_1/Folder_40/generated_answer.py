def remove_repeat_chars(input_string):
    repeat_chars = [char for char in input_string[:4] if input_string.count(char) > 1]
    for char in repeat_chars:
        input_string = input_string.replace(char, '')
    return input_string