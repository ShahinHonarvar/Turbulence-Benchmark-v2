def remove_repeat_chars(input_string):
    chars_to_remove = set()
    sub_string = input_string[13:91]
    for char in sub_string:
        if input_string.count(char) > 1:
            chars_to_remove.add(char)
    result_string = input_string
    for char in chars_to_remove:
        result_string = result_string.replace(char, '')
    return result_string