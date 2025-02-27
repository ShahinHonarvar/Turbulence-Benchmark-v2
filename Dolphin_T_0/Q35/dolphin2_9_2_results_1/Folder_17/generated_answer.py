def remove_repeat_chars(input_string):
    chars_to_remove = {}
    for i in range(73, 84):
        if input_string[i] in chars_to_remove:
            continue
        for j in range(i + 1, 84):
            if input_string[i] == input_string[j]:
                chars_to_remove[input_string[i]] = True
                break
    return_string = ''
    for char in input_string:
        if char not in chars_to_remove:
            return_string += char
    return return_string