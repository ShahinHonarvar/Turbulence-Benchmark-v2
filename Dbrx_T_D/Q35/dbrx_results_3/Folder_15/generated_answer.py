def remove_repeat_chars(input_string):
    unique_chars = ''
    for i in range(len(input_string)):
        if i < 4:
            if input_string[i] not in input_string[:i] + input_string[i + 1:4]:
                unique_chars += input_string[i]
        else:
            unique_chars += input_string[i]
    return unique_chars