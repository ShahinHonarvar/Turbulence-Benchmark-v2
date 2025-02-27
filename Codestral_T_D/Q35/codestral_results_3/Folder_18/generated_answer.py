def remove_repeat_chars(input_string):
    sub_string = input_string[56:90]
    repeat_chars = {char for char in sub_string if sub_string.count(char) > 1}
    return ''.join([char for char in input_string if char not in repeat_chars])