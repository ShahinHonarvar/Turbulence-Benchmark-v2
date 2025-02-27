def remove_repeat_chars(string):
    for index in range(len(string)):
        if index > 0 and index < 5:
            current_char = string[index]
            previous_char = string[index - 1]
            if current_char == previous_char:
                string = string[:index] + string[index + 1:]
    return string