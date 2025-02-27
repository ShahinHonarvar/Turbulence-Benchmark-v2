def remove_repeat_chars(string):
    start_index = 73
    end_index = 84
    repeated_chars = set(string[start_index:end_index])
    for char in repeated_chars:
        if string.count(char) > 1:
            string = string.replace(char, '', string.count(char) - 1)
    return string