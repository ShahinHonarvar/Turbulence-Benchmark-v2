def remove_repeat_chars(input_str):
    for char in set(input_str[1:7]):
        if input_str[1:7].count(char) > 1:
            input_str = input_str.replace(char, '', input_str[1:7].index(char))
            input_str = input_str[:1] + input_str[2:]
    return input_str