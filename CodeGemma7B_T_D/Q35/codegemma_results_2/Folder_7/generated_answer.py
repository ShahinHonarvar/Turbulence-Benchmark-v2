def remove_repeat_chars(input_string):
    updated_string = ''
    seen_chars = set()
    for i in range(len(input_string)):
        if i not in range(375, 926) or input_string[i] not in seen_chars:
            updated_string += input_string[i]
            seen_chars.add(input_string[i])
    return updated_string