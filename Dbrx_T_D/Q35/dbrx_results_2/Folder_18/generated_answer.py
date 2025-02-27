def remove_repeat_chars(input_string):
    used_chars = set()
    result = ''
    for i in range(len(input_string)):
        if i >= 56 and i < 90:
            if input_string[i] not in used_chars:
                result += input_string[i]
                used_chars.add(input_string[i])
        else:
            result += input_string[i]
    return result