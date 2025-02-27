def remove_repeat_chars(input_string):
    for char in set(input_string[49:75]):
        if input_string[49:75].count(char) > 1:
            while True:
                try:
                    input_string = input_string.replace(char, '', 1)
                except IndexError:
                    break
    return input_string