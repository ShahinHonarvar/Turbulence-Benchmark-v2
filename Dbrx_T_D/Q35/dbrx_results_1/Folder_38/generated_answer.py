def remove_repeat_chars(input_string):
    used_characters = set()
    result = ''
    for i in range(len(input_string)):
        if i < 36 or i >= 85:
            result += input_string[i]
        elif input_string[i] not in used_characters:
            used_characters.add(input_string[i])
            result += input_string[i]
    return result